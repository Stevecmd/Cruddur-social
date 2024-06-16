from flask import Flask, request
from flask_cors import CORS, cross_origin
import os
import logging

from services.home_activities import *
from services.notifications_activities import *
from services.user_activities import *
from services.create_activity import *
from services.create_reply import *
from services.search_activities import *
from services.message_groups import *
from services.messages import *
from services.create_message import *
from services.show_activity import *

# HoneyComb 
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# Import AWS X-Ray SDK
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

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
xray_url = os.getenv("AWS_XRAY_URL", "127.0.0.1:2000")
logging.info(f'XRay URL: {xray_url}')
xray_recorder.configure(service='backend-flask', dynamic_naming=xray_url)
XRayMiddleware(app, xray_recorder)

@app.route("/api/message_groups", methods=['GET'])
def data_message_groups():
  with tracer.start_as_current_span("data_message_groups"):
    user_handle  = 'andrewbrown'
    model = MessageGroups.run(user_handle=user_handle)
    if model['errors'] is not None:
      return model['errors'], 422
    else:
      return model['data'], 200

@app.route("/api/messages/@<string:handle>", methods=['GET'])
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

@app.route("/api/activities/home", methods=['GET'])
def data_home():
    with tracer.start_as_current_span("data_home"):
        data = HomeActivities.run()
        return data, 200

@app.route("/api/activities/notifications", methods=['GET'])
def data_notifications():
  with tracer.start_as_current_span("data_notifications"):
    data = NotificationsActivities.run()
    return data, 200

@app.route("/api/activities/@<string:handle>", methods=['GET'])
@xray_recorder.capture('activities_users')
def data_handle(handle):
  with tracer.start_as_current_span("data_handle"):
    model = UserActivities.run(handle)
    if model['errors'] is not None:
      return model['errors'], 422
    else:
      return model['data'], 200

@app.route("/api/activities/search", methods=['GET'])
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
def data_show_activity(activity_uuid):
    with tracer.start_as_current_span("data_show_activity"):
        data = ShowActivity.run(activity_uuid=activity_uuid)
        return data, 200

@app.route("/api/activities/<string:activity_uuid>/reply", methods=['POST','OPTIONS'])
@cross_origin()
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
