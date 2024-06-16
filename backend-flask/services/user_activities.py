from datetime import datetime, timedelta, timezone
from opentelemetry import trace

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

        # Instrumentation: Start tracing span for user activities operation
        with tracer.start_as_current_span("user-activities"):
            span = trace.get_current_span()
            span.set_attribute("user_handle", user_handle)
            span.set_attribute("has_errors", bool(model['errors']))
            span.set_attribute("result_length", len(model.get('data', [])))

        return model
