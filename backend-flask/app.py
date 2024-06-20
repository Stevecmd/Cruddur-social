from flask import Flask, request
from flask_cors import CORS, cross_origin
import os
import logging

# Cloudwatch
import watchtower
from time import strftime

# # Configuring Logger to Use CloudWatch
# LOGGER = logging.getLogger(__name__)
# LOGGER.setLevel(logging.DEBUG)
# console_handler = logging.StreamHandler()
# cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
# LOGGER.addHandler(console_handler)
# LOGGER.addHandler(cw_handler)
# LOGGER.info('Test log')

from services.home_activities import HomeActivities
from services.notifications_activities import *
from services.user_activities import *
from services.create_activity import *
from services.create_reply import *
from services.search_activities import *
from services.message_groups import *
from services.messages import *
from services.create_message import *
from services.show_activity import ShowActivities

# HoneyComb 
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# # New-relic
# from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
# from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import BatchSpanProcessor
# from opentelemetry.sdk.resources import Resource
# from opentelemetry.semconv.resource import ResourceAttributes

# # New Relic Exporter
# from opentelemetry.exporter.newrelic import NewRelicSpanExporter

# # Initialize tracing with New Relic Exporter
# provider = TracerProvider(resource=Resource.create({
#     ResourceAttributes.SERVICE_NAME: "backend-flask"
# }))

# # New Relic Span Exporter
# newrelic_exporter = NewRelicSpanExporter(
#     insert_key=os.getenv('NEW_RELIC_INSERT_KEY'),  # New Relic Insert Key
#     service_name="backend-flask"
# )

# processor = BatchSpanProcessor(newrelic_exporter)
# provider.add_span_processor(processor)
# trace.set_tracer_provider(provider)
# tracer = trace.get_tracer(__name__)

# Import AWS X-Ray SDK
# from aws_xray_sdk.core import xray_recorder
# from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

# ---- Rollbar -----
from time import strftime
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# HoneyComb -----------
# Initialize tracing
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# Add SimpleSpanProcessor to show spans in STDOUT
simple_processor = SimpleSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(simple_processor)

# CORS setup
frontend = os.getenv('FRONTEND_URL')
backend = os.getenv('BACKEND_URL')
logging.info(f'Frontend URL: {frontend}')
logging.info(f'Backend URL: {backend}')
origins = [frontend, backend]
cors = CORS(app, resources={r"/api/*": {"origins": origins}},
            expose_headers="location,link",
            allow_headers="content-type,if-modified-since",
            methods="OPTIONS,GET,HEAD,POST")

# Instrument Flask app
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

# Xray
# xray_url = os.getenv("AWS_XRAY_URL", "127.0.0.1:2000")
# logging.info(f'XRay URL: {xray_url}')
# xray_recorder.configure(service='backend-flask', dynamic_naming=xray_url)
# XRayMiddleware(app, xray_recorder)

# # ------- Cloudwatch Logs ----------
# @app.after_request
# def after_request(response):
#     timestamp = strftime('[%Y-%b-%d %H:%M]')
#     LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
#     return response

# Initialize rollbar flag
rollbar_initialized = False

# Rollbar ---------
rollbar_access_token = os.getenv('ROLLBAR_ACCESS_TOKEN')

if not rollbar_access_token:
    logging.error("ROLLBAR_ACCESS_TOKEN not set")
else:
    logging.info(f"ROLLBAR_ACCESS_TOKEN is set to {rollbar_access_token}")
    rollbar.init(
        rollbar_access_token,
        'production',
        root=os.path.dirname(os.path.realpath(__file__)),
        allow_logging_basic_config=False
    )
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)
    rollbar_initialized = True

@app.before_request
def init_rollbar():
    global rollbar_initialized
    if not rollbar_initialized:
        """init rollbar module"""
        rollbar.init(
            # access token
            rollbar_access_token,
            # environment name
            'production',
            # server root directory, makes tracebacks prettier
            root=os.path.dirname(os.path.realpath(__file__)),
            # flask already sets up logging
            allow_logging_basic_config=False)

        # send exceptions from `app` to rollbar, using flask's signal system.
        got_request_exception.connect(rollbar.contrib.flask.report_exception, app)
        rollbar_initialized = True

@app.route('/rollbar/test')
def rollbar_test():
    rollbar.report_message('Hello World!', 'warning')
    return "Hello World!"

@app.route("/api/activities/notifications", methods=['GET'])
# @xray_recorder.capture('data_notifications')
def data_notifications():
    with tracer.start_as_current_span("data_notifications"):
        data = NotificationsActivities.run()
        return data, 200

@app.route("/api/message_groups", methods=['GET'])
# @xray_recorder.capture('data_message_groups')
def data_message_groups():
    with tracer.start_as_current_span("data_message_groups"):
        user_handle  = 'andrewbrown'
        model = MessageGroups.run(user_handle=user_handle)
        if model['errors'] is not None:
            return model['errors'], 422
        else:
            return model['data'], 200

@app.route("/api/messages/@<string:handle>", methods=['GET'])
# @xray_recorder.capture('data_messages')
def data_messages(handle):
    with tracer.start_as_current_span("data_messages"):
        user_sender_handle = 'andrewbrown'
        user_receiver_handle = request.args.get('user_reciever_handle')

        model = Messages.run(user_sender_handle=user_sender_handle, user_receiver_handle=user_receiver_handle)
        if model['errors'] is not None:
            return model['errors'], 422
        else:
            return model['data'], 200
        return

@app.route("/api/messages", methods=['POST','OPTIONS'])
@cross_origin()
# @xray_recorder.capture('data_create_message')
def data_create_message():
    with tracer.start_as_current_span("data_create_message"):
        user_sender_handle = 'andrewbrown'
        user_receiver_handle = request.json['user_receiver_handle']
        message = request.json['message']

        model = CreateMessage.run(message=message,user_sender_handle=user_sender_handle,user_receiver_handle=user_receiver_handle)
        if model['errors'] is not None:
            return model['errors'], 422
        else:
            return model['data'], 200
        return

@app.route("/api/activities/home", methods=["GET"])
def data_home():
    with tracer.start_as_current_span("data_home"):
        data = HomeActivities.run()
        return data, 200

# @app.route("/api/activities/notifications", methods=['GET'])
# # @xray_recorder.capture('data_notifications')
# def data_notifications():
#     with tracer.start_as_current_span("data_notifications"):
#         data = NotificationsActivities.run()
#         return data, 200

@app.route("/api/activities/@<string:handle>", methods=['GET'])
# @xray_recorder.capture('data_handle')
# @xray_recorder.capture('activities_users')
def data_handle(handle):
    with tracer.start_as_current_span("data_handle"):
        model = UserActivities.run(handle)
        if model['errors'] is not None:
            return model['errors'], 422
        else:
            return model['data'], 200

@app.route("/api/activities/search", methods=['GET'])
# @xray_recorder.capture('data_search')
def data_search():
    with tracer.start_as_current_span("data_search"):
        term = request.args.get('term')
        model = SearchActivities.run(term)
        if model['errors'] is not None:
            return model['errors'], 422
        else:
            return model['data'], 200

@app.route("/api/activities", methods=['POST','OPTIONS'])
@cross_origin()
# @xray_recorder.capture('data_activities')
def data_activities():
    with tracer.start_as_current_span("data_activities"):
        user_handle = 'andrewbrown'
        message = request.json['message']
        ttl = request.json['ttl']
        model = CreateActivity.run(message, user_handle, ttl)
        if model['errors'] is not None:
            return model['errors'], 422
        else:
            return model['data'], 200

@app.route("/api/activities/<string:activity_uuid>", methods=['GET'])
# @xray_recorder.capture('data_show_activity')
def data_show_activity(activity_uuid):
    with tracer.start_as_current_span("data_show_activity"):
        data = ShowActivity.run(activity_uuid=activity_uuid)
        return data, 200

@app.route("/api/activities/<string:activity_uuid>/reply", methods=['POST','OPTIONS'])
@cross_origin()
# @xray_recorder.capture('data_activities_reply')
def data_activities_reply(activity_uuid):
    with tracer.start_as_current_span("data_activities_reply"):
        user_handle = 'andrewbrown'
        message = request.json['message']
        model = CreateReply.run(message, user_handle, activity_uuid)
        if model['errors'] is not None:
            return model['errors'], 422
        else:
            return model['data'], 200

if __name__ == "__main__":
    app.run(debug=True)
