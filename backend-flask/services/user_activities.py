from datetime import datetime, timedelta, timezone
from opentelemetry import trace
from aws_xray_sdk.core import xray_recorder

tracer = trace.get_tracer("user.activities")

class UserActivities:
    def run(user_handle):
        model = {
            'errors': None,
            'data': None
        }

        # Validate user_handle
        if user_handle is None or len(user_handle) < 1:
            model['errors'] = ['blank_user_handle']
        else:
            now = datetime.now(timezone.utc).astimezone()
            results = [{
                'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                'handle': 'Andrew Brown',
                'message': 'Cloud is fun!',
                'created_at': (now - timedelta(days=1)).isoformat(),
                'expires_at': (now + timedelta(days=31)).isoformat()
            }]
            model['data'] = results

        try:
            # Start an X-Ray subsegment
            subsegment = xray_recorder.begin_subsegment('mock-data')
            # Add metadata to the subsegment
            metadata_dict = {
                "now": now.isoformat(),
                "results-size": len(model['data'])
            }
            subsegment.put_metadata('key', metadata_dict, 'namespace')
        finally:
            # End the X-Ray subsegment
            xray_recorder.end_subsegment()

        # Instrumentation: Start tracing span for user activities operation
        with tracer.start_as_current_span("user-activities"):
            span = trace.get_current_span()
            span.set_attribute("user_handle", user_handle)
            span.set_attribute("has_errors", bool(model['errors']))
            span.set_attribute("result_length", len(model.get('data', [])))

        return model
