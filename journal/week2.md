# Week 2 — Distributed Tracing
This was technically the third week of the Bootcamp. 

(The Hyperlinks in the table below link to the training videos)
<hr/>

| Homework      | Completed     | Not Completed  |
| ------------- |:-------------:| -----:|
| [Create your Free HoneyComb.io account](https://www.youtube.com/watch?v=7IwtVLfSD0o&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=10)   | ✔ |  |
| [Create your Free RollBar account](https://www.youtube.com/watch?v=Lpm6oAP3Fb0&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=11)  | ✔     |    |
| [Watch Week 2 Live-Stream Video](https://www.youtube.com/watch?v=2GD9xCzRId4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=30) | ✔      |   |
| [Watch Chirag Week 2 - Spending Considerations (Coming Soon)](https://www.youtube.com/watch?v=2W3KeqCjtDY )|✔      |   |
| [Watched Ashish's Week 2 - Observability Security Considerations](https://www.youtube.com/watch?v=bOf4ITxAcXc&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=31)|✔      |   |
| [Instrument Honeycomb with OTEL](https://www.youtube.com/watch?v=2GD9xCzRId4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=30)|    ✔  |   |
| [Instrument AWS X-Ray](https://www.youtube.com/watch?v=n2DTsuBrD_A&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=32)  | ✔   |   |
| [Configure custom logger to send to CloudWatch Logs](https://www.youtube.com/watch?v=ipdFizZjOF4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=33) |✔      |   |
| [Integrate Rollbar and capture and error](https://www.youtube.com/watch?v=xMBDAb5SEU4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=35)| ✔   |   |


>**Below is a step by step break down of my work. Use the Table below to jump to specific sections.**


|    | Table of Contents                                                                                                                                                                          |    |                                                                                                                                                                             |
|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | * [Honeycomb environment](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#honeycomb-environment)                                                          | 25 | * [Query duration heatmap](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#query-duration-heatmap)                                         |
| 2  | * [Instrument Honeycomb with OTEL](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#instrument-honeycomb-with-otel)                                        | 26 | * [Magnifying the Query results](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#magnifying-the-query-results)                             |
| 3  | * [Open Telemetry (OTEL) installation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#open-telemetry-otel-installation)                                  | 27 | * [X-Ray](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#x-ray)                                                                           |
| 4  | * [Updating App.py to include HoneyComb configuration](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#updating-apppy-to-include-honeycomb-configuration) | 28 | * [Adding X-Ray to requirements](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#adding-x-ray-to-requirements)                             |
| 5  | * [HoneyComb instrumentation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#honeycomb-instrumentation)                                                  | 29 | * [Additional ports -> x-ray daemon](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#additional-ports---x-ray-daemon)                      |
| 6  | * [Setting up the HoneyComb API Key](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#setting-up-the-honeycomb-api-key)                                    | 30 | * [X-Ray Install](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#x-ray-install)                                                           |
| 7  | * [Backend Logs](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#backend-logs)                                                                            | 31 | * [X-Ray Group ARN on AWS](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#x-ray-group-arn-on-aws)                                         |
| 8  | * [Automating of the opening of backend ports](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#automating-of-the-opening-of-backend-ports)                | 32 | * [RollBar](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#rollbar)                                                                       |
| 9  | * [Cruddur returning API endpoint](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#cruddur-returning-api-endpoint)                                        | 33 | * [Rollbar account creation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#rollbar-account-creation)                                     |
| 10 | * [API endpoint on terminal](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#api-endpoint-on-terminal)                                                    | 34 | * [Selecting Flask as the app type in Rollbar](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#selecting-flask-as-the-app-type-in-rollbar) |
| 11 | * [Succesfull connection - JSON data](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#succesfull-connection---json-data)                                  | 35 | * [Adding Rollbar support - Blinker](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#adding-rollbar-support---blinker)                     |
| 12 | * [Whoami-glitch.me](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#whoami-glitchme)                                                                     | 36 | * [Creating a Logger on the backend](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#creating-a-logger-on-the-backend)                     |
| 13 | * [OTEL configuration](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#otel-configuration)                                                                | 37 | * [Testing access to the Rollbar page](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#testing-access-to-the-rollbar-page)                 |
| 14 | * [Working HoneyComb Queries](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#working-honeycomb-queries)                                                  | 38 | * [Setting the Rollbar Access token](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#setting-the-rollbar-access-token)                     |
| 15 | * [HoneyComb Traces](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#honeycomb-traces)                                                                    | 39 | * [Setting the Rollbar Access token in Docker](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#setting-the-rollbar-access-token-in-docker) |
| 16 | * [HoneyComb Trace Review](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#honeycomb-trace-review)                                                        | 40 | * [Accessing the test Rollbar webpage](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#accessing-the-test-rollbar-webpage)                 |
| 17 | * [Adding a span in homeactivities](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#adding-a-span-in-homeactivitiespy)                                    | 41 | * [Rollbar Logs Success](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#rollbar-logs-success)                                             |
| 18 | * [HoneyComb trace of the New Span](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#honeycomb-trace-of-the-new-span)                                      | 42 | * [Rollbar Report](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#rollbar-report)                                                         |
| 19 | * [Creating a custom Span](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#creating-a-custom-span)                                                        | 43 | * [Rollbar Logged occurences](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#rollbar-logged-occurences)                                   |
| 20 | * [Creating a query on HoneyComb](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#creating-a-query-on-honeycomb)                                          | 44 | * [Rollbar Error Report](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#rollbar-error-report)                                             |
| 21 | * [Running Traces on HoneyComb](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#running-traces-on-honeycomb)                                              | 45 | * [Rollbar Error Report Specifics](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#rollbar-error-report-specifics)                         |
| 22 | * [Traces report on mock data](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#traces-report-on-mock-data)                                                |    |                                                                                                                                                                             |
| 23 | * [Custom Trace](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#custom-trace)                                                                            |    |                                                                                                                                                                             |
| 24 | * [New Query](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week2.md#new-query)                                                                                  |    |                                                                                                                                                                             |

## Honeycomb environment

### Setup

1. On the [Honeycomb website](https://www.honeycomb.io/), create a new environment named `Cruddur-social`, and obtain the corresponding API key.
   For detailed instructions, refer to the [Honeycomb Documentation](https://docs.honeycomb.io/).

2. Set the `Honeycomb API Key `as an environment variable in Gitpod using these commands: 
```bash
export HONEYCOMB_API_KEY="<your API key>"
gp env HONEYCOMB_API_KEY="<your API key>"

export HONEYCOMB_SERVICE_NAME="Cruddur-social"
gp env HONEYCOMB_SERVICE_NAME="Cruddur-social"

```
<bold> Make sure to include the quotation marks.<bold /> <br />

3. Confirm the environment variables `env vars` have been set:
```sh
      env | grep HONEY
```

4. Use your API key in the `backend-flask` -> `docker-compose.yml` file. Under the `backend-flask` service, add the following code:

```yaml
backend-flask:
    environment:
      OTEL_SERVICE_NAME: 'backend-flask'
      OTEL_EXPORTER_OTLP_ENDPOINT: "https://api.honeycomb.io"
      OTEL_EXPORTER_OTLP_HEADERS: "x-honeycomb-team=${HONEYCOMB_API_KEY}"
```

### Instrumentation

1. Add the following packages to `backend-flask` -> `requirements.txt` to install the required packages for Open Telemetry (OTEL) services:

```txt
  opentelemetry-api 
  opentelemetry-sdk 
  opentelemetry-exporter-otlp-proto-http 
  opentelemetry-instrumentation-flask 
  opentelemetry-instrumentation-requests

```

<br />

2. Install the required packages by running the following command from within `backend-flask`:

```sh
      pip install -r requirements.txt
```

3. In `backend-flask` -> `app.py`, add the following code after the `from services...` import statement but above `app = Flask(__name__)`:

```py
# Honeycomb ------------
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
```
- **Initialize tracing and an exporter that can send data to Honeycomb**
```python
  # Honeycomb ------------
  # Initialize tracing and an exporter that can send data to Honeycomb
  provider = TracerProvider()
  processor = BatchSpanProcessor(OTLPSpanExporter())
  provider.add_span_processor(processor)
  trace.set_tracer_provider(provider)
  tracer = trace.get_tracer(__name__)

```
<br />

- **Add the code below inside the 'app' to Initialize automatic instrumentation with Flask**
  <br />
```python
# Honeycomb ------------
# Initialize automatic instrumentation with Flask
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

frontend = os.getenv('FRONTEND_URL')
backend = os.getenv('BACKEND_URL')
origins = [frontend, backend]
cors = CORS(
  app, 
  resources={r"/api/*": {"origins": origins}},
  expose_headers="location,link",
  allow_headers="content-type,if-modified-since",
  methods="OPTIONS,GET,HEAD,POST"
)
```

#### Spans and Traces in Open Telemetry

- A span is a unit of work that is executed within a trace. Spans are used to track the execution of your application, and they can be used to collect performance data, identify bottlenecks, and troubleshoot problems. <br />

- A trace is a collection of spans. Traces are used to track the flow of execution through your application. They can be used to identify the root cause of problems, and they can be used to visualize the performance of your application. <br />

When traces are sent to Honeycomb, the name of the Tracer is turned into the library.name field, which can be used to show all spans created from a particular tracer.

#### Adding spans and attributes to tracers
To create a span, you need to get a Tracer. A Tracer is a factory for creating spans. When you create a Tracer, you need to give it a name as a string. This string is the only required parameter. <br />

Once you have set up tracing, you can add spans and attributes to tracers. A span is a unit of work that is executed within a trace. An attribute is a piece of data that can be attached to a span. <br />

To add a span and attribute to a tracer, you can refer to the following:
1. Create a trace by adding the following code on `app.py`:

```python
      from opentelemetry import trace
      tracer = trace.get_tracer("home.activities")
```
<br />

2. Inside the `HomeActivities` class, Create a span and name it. This is used to initiate a new span.
```py

class HomeActivities:
  def run():
    with tracer.start_as_current_span("home-activities-mock-data"):

```
3. Allow access to the current active span:
```py

      span = trace.get_current_span()

```

4. Implement additional tracing and metadata capabilities
```py

      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      span.set_attribute("app.result_length", len(results))

```

The full code to create span and attribute is as below, replace the following code in `home_activities.py`:

```python
from datetime import datetime, timedelta, timezone
from opentelemetry import trace

tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run():

    with tracer.start_as_current_span("home-activites-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())
      results = [{
        'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
        'handle':  'Andrew Brown',
        'message': 'Cloud is fun!',
        'created_at': (now - timedelta(days=2)).isoformat(),
        'expires_at': (now + timedelta(days=5)).isoformat(),
        'likes_count': 5,
        'replies_count': 1,
        'reposts_count': 0,
        'replies': [{
          'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
          'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
          'handle':  'Worf',
          'message': 'This post has no honor!',
          'likes_count': 0,
          'replies_count': 0,
          'reposts_count': 0,
          'created_at': (now - timedelta(days=2)).isoformat()
        }],
      },
      {
        'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
        'handle':  'Worf',
        'message': 'I am out of prune juice',
        'created_at': (now - timedelta(days=7)).isoformat(),
        'expires_at': (now + timedelta(days=9)).isoformat(),
        'likes': 0,
        'replies': []
      },
      {
        'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
        'handle':  'Garek',
        'message': 'My dear doctor, I am just simple tailor',
        'created_at': (now - timedelta(hours=1)).isoformat(),
        'expires_at': (now + timedelta(hours=12)).isoformat(),
        'likes': 0,
        'replies': []
      }
      ]
    span.set_attribute("app.result_length", len(results)) 
    return results
```

In this code, we are creating a span named `home-activities-mock-data` and setting an attribute named `app.now`. The value of the attribute is the current time, as returned by the `datetime.now()` function. <br />

Once we have added a span and attribute to a tracer, we can view the results on the Honeycomb website. <br />

To do this, you need to launch the app and browse the backend endpoint and add the address `/api/activities/home`. 

##### Additional Span Example

```python
span.set_attribute("app.now", now.isoformat())
```

Add the code below to `home_activities.py` for testing:
```py
LOGGER.info("HomeActivities")
```

Once you receive info on Honeycomb, you can comment out the following code for cleaner logs:
```py
#def run(Logger):
   #Logger.info("HomeActivities")
```

### Honeycomb for Better Observability
Having more observability leads to a better understanding of your errors and how to resolve them.

1. Import the `tracer` and `trace` objects from the `opentelemetry` library.

```python
from opentelemetry import trace
tracer = trace.get_tracer(__name__)
```
The code above automates the opening of the given ports. <br />

2. Create a new span with the `tracer.start_as_current_span()` method.
```py
span = tracer.start_as_current_span("home_activity")
```
`File: home_activity.py`

```
This setup ensures that all necessary dependencies for both the frontend and backend components are installed and ready for use.

4. Create nested spans with the `tracer.start_as_current_span()` method.
```py
with tracer.start_as_current_span("flaskfunc") as inner_span:
    inner_span.set_attribute("inner", True)
    span.set_attribute("user.id", user.get("user"))
    with tracer.start_as_current_span("flaskfuncfunc") as sub_inner_span:
        span.set_attribute("user.id", user.get("userID"))
```

5. Set the attributes of nested spans.

```py
inner_span.set_attribute("inner", True)
span.set_attribute("user.id", user.get("user"))
```

6. Add events to the spans.
```py
current_span = trace.get_current_span()
current_span.add_event("Event is Working!")
```

Additionally, You can aim to intrument the following use cases.

1. **Measure Request Duration:** Track the time taken for each API request to identify slow endpoints and performance bottlenecks.
2. **Track Errors:** Monitor and analyze error occurrences to quickly detect and resolve issues.
3. **Monitor User Behavior:** Instrument user actions like login/logout to understand how users interact with your app.
4. **Analyze Database Queries:** Monitor database query execution time and frequency to optimize performance.
5. **Track API Endpoint Usage:** Identify frequently accessed endpoints to understand critical app areas.
6. **Monitor Resource Utilization:** Measure CPU, memory, and system resource usage to identify resource-intensive parts.
7. **Analyze External Service Calls:** Monitor response times of interactions with external services for potential issues.
8. **Capture Custom Business Events:** Instrument app-specific events to gain insights into user behavior and conversions.
9. **Track Feature Usage:** Monitor feature flags or A/B tests to understand their impact on user engagement.
10. **Monitor Geolocation Data:** Track location-related events for insights based on geographical locations.
<br>

The key is to choose instrumentation that aligns with your specific application's goals and requirements.

### Heatmap in Honeycomb

A heatmap is a graphical representation that provides a visual overview of the distribution and density of events over a specified period. It displays aggregated metrics related to service performance, request latency, error rates, or other custom attributes.

1. Open the menu on Left-Hand Side and select "New Query" to start building a new query.
2. In the query editor, set the visualization options to `HEATMAP(duration_ms)` and `"P90(duration_ms)` for the desired analysis.
3. Once the options are configured, run the query to generate the heatmap visualization.

You can zoom in and out on the heatmap, allowing you to see the details more clearly.

## Honeycomb Who Am I? 
The **Honeycomb Who Am I?** project is designed to provide insights into what system is this.

When you have the tools spreads out before you, it's easy to lose track of what was this for and which is assigned to what task, so the projet comes along.

1. **Accessing the Tool:**
Navigate to the URL provided [Who-Am-I](https://honeycomb-whoami.glitch.me/) to access the "Honeycomb Who Am I?" tool interface.

2. **API Key Input:**
You will be prompted to provide your Honeycomb API key. Copy and paste the provided API key (`Kk4cyhR9ksCxNbrg6zyCyA`) into the designated field.

3. **Submit and Authenticate:**
Click on the "Submit" button after entering the API key. This will authenticate your access to the Honeycomb platform.

4. **Understanding the Context:**
The tool will provide information about the team, environment, and access privileges associated with the provided API key. For example:

- Team: CRUDDUR-SOCIAL Project
- Environment: test
- Access: List of available Honeycomb features and access levels.

5. **Performing Troubleshooting:**
Once authenticated, you can use the tool to troubleshoot specific issues related to your application or system. Here are the steps to follow:

- a. **Define the Problem:** Clearly define the issue you want to investigate. For example, you might want to understand why certain API requests are slow or why errors are occurring in your application.
- b. **Instrumentation:** Ensure that your application is correctly instrumented to send traces and telemetry data to Honeycomb. If not already done, refer to Honeycomb's documentation to set up the necessary configurations.
- c. **Filter Data:** Use the tool's filtering options to narrow down the data you want to analyze. You can focus on specific time frames, endpoints, services, or other relevant criteria.
- d. **Explore Traces:** Dive into individual traces to understand the flow of requests through your system. Look for patterns, anomalies, or any indications of errors.
- e. **Visualize Performance Metrics:** Utilize the tool's built-in visualizations to analyze performance metrics such as response times, latency, error rates, and more. This can help you identify areas that require attention.
- f. **Collaborate and Share:** If you are working in a team, share the tool's results and insights with your colleagues to facilitate collaboration and problem-solving.
- g. **Iterative Troubleshooting:** Address the issues you find through the tool's analysis, and repeat the process iteratively to refine your investigation until you identify and resolve the root cause of the problem.

The tool serves as a powerful resource to gain deeper insights into your system's behavior and performance. 

For a full walkthrough on how to add `Honeycomb`, check out the docs at:
[HoneyComb Docs](https://docs.honeycomb.io/getting-data-in/opentelemetry/python-distro/) <br/>

Specifically look at **trace**, **span** and **Adding attributes to spans**.

## AWS X-RAY
Amazon has another service called X-RAY which is helpful in tracing requests by microservices. analyzes and debugs application running on distributed environments. 

### Resources:
[AWS X-Ray](https://pages.github.com/](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html))
<br />

[AWS X-Ray Best practices](https://pages.github.com/](https://stackoverflow.com/questions/54236375/what-are-the-best-practises-for-setting-up-x-ray-daemon))
<br />

[AWS X-ray GitHub repo](https://github.com/aws/aws-xray-sdk-python)
[Hashnode Article by Olga](https://olley.hashnode.dev/aws-free-cloud-bootcamp-instrumenting-aws-x-ray-subsegments)

check the env var for the AWS region using the following command:
```sh
env | grep AWS_REGION
```
If there is no result run:
```sh
export AWS_REGION="<chosen region>"
gp env AWS_REGION="<chosen region>"
```
Check that your authentication details are still in place and that you are able to connect to AWS:
```py
aws sts get-caller-identity
```
The prompt should return data similar to:
```py
      "UserId": "<AccountName>"
      "Account": "<AccountNumber>"
      "Arn": "<AccountARN>"
```
<br />

- To get your application traced in AWS X-RAY you need to install `aws-xray-sdk` module. You can do this by running the commands below:
```
pip install aws-xray-sdk
```
In the `backend-flask` > `requirements.txt`, insert the following:
```py
aws-xray-sdk
```
Additionally, to install all the dependencies via Python package manager run:
```sh
pip install -r requirements.txt
```
To manually install `x-ray` run:
`pip install aws-xray-sdk`

Make sure to create segments and subsegments by following the instructional videos. 

Insert the following code inside the `app.py`:
```python
# Xray
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
```
```python
# Xray
xray_url = os.getenv("AWS_XRAY_URL")
xray_recorder.configure(service='backend-flask', dynamic_naming=xray_url)
XRayMiddleware(app, xray_recorder)
```
Modify the code in `app.py` as follows:
```py
@app.route("/api/activities/home", methods=['GET'])
@xray_recorder.capture('activities_home')
def data_home():
  data = HomeActivities.run()
  return data, 200
```

around line 127:
```py
@app.route("/api/activities/@<string:handle>", methods=['GET'])
@xray_recorder.capture('activities_users')
def data_handle(handle):
  model = UserActivities.run(handle)
  if model['errors'] is not None:
```

around line 160:
```py
@app.route("/api/activities/<string:activity_uuid>", methods=['GET'])
@xray_recorder.capture('activities_show')
```

- Created our own Sampling Rule name `Cruddur`. This code was written in `aws/json/xray.json` file:
```json
{
  "SamplingRule": {
      "RuleName": "Cruddur",
      "ResourceARN": "*",
      "Priority": 9000,
      "FixedRate": 0.1,
      "ReservoirSize": 5,
      "ServiceName": "backend-flask",
      "ServiceType": "*",
      "Host": "*",
      "HTTPMethod": "*",
      "URLPath": "*",
      "Version": 1
  }
}
```
- **To create a new group for tracing and analyzing errors and faults in a Flask application.**

<br> Add a sampling group to monitor log events by running this in the terminal:
```py
aws xray create-group \
   --group-name "Cruddur" \
   --filter-expression "service(\"backend-flask\")"
```
The above code is useful for setting up monitoring for a specific Flask service using AWS X-Ray. It creates a group that can be used to visualize and analyze traces for that service, helping developers identify and resolve issues more quickly. We are specifically monitoring backend-flask.

Then run this command to get the above code executed 
```bash
aws xray create-sampling-rule --cli-input-json file://aws/json/xray.json
```

- **Install Daemon Service**
Add the code below to `docker-compose.yml` file.
```yaml
 xray-daemon:
    image: "amazon/aws-xray-daemon"
    environment:
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
      AWS_REGION: "us-east-1"
    command:
      - "xray -o -b xray-daemon:2000"
    ports:
      - 2000:2000/udp
```
Also add Environment Variables in the `docker-compose.yml` file under environment in `backend-flask`:
```yaml
   AWS_XRAY_URL: "*4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}*"
   AWS_XRAY_DAEMON_ADDRESS: "xray-daemon:2000"
   AWS_DEFAULT_REGION: "${AWS_DEFAULT_REGION}"
```

The full code for `user_activities.py` service having implemented x-ray should be similar to:
```py
from datetime import datetime, timedelta, timezone
class UserActivities:
  def run(user_handle):
    model = {
      'errors': None,
      'data': None
    }

    now = datetime.now(timezone.utc).astimezone()

    if user_handle == None or len(user_handle) < 1:
      model['errors'] = ['blank_user_handle']
    else:
      now = datetime.now()
      results = [{
        'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
        'handle':  'Andrew Brown',
        'message': 'Cloud is fun!',
        'created_at': (now - timedelta(days=1)).isoformat(),
        'expires_at': (now + timedelta(days=31)).isoformat()
      }]
      model['data'] = results
    return model
```
![AWS X-ray segements sent](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%202/AWS-X-ray/terminal_segments_sent.JPG)
![AWS X-ray Trace map](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%202/AWS-X-ray/trace-map.JPG)
![AWS X-ray Traces](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%202/AWS-X-ray/traces.JPG)
=======
To ensure x-ray is running use:
```sh
docker ps | grep xray-daemon
```
## Debugging
There is a lack of connectivity between `backens-flask` and `aws-x-ray-daemon` containsers. <br />
I first created a script to check connectivity named `x-ray-connection-check.py`

```py

#!/usr/bin/env python3

import socket

def check_xray_connectivity():
    sock = None
    try:
        xray_host = "xray-daemon"
        xray_port = 2000
        sock = socket.create_connection((xray_host, xray_port), timeout=5)
        print("Connection to xray-daemon on port 2000 succeeded")
    except socket.error as err:
        print(f"Connection to xray-daemon on port 2000 failed: {err}")
    finally:
        if sock:
            sock.close()

check_xray_connectivity()

```

Additionally I also attached the `backend-flask` container so as to debug it.
Once connected I installed `ping`
```sh
apt-get update
apt-get install -y iputils-ping netcat
```
check network connectivity:
```sh
ping xray-daemon
nc -zv xray-daemon 2000
```
## #3 CloudWatch
For CLoudWatch install `watchtower` then input the imports: `watchtower`, `logging` and `strftime from time`.

In `backend-flask requirements.text`, insert the following text:
```yaml
watchtower
```

To install all dependencies>> <bold>`only necessary this time as it will be run automatically via docker compose`</bold>

```sh
pip install -r requirements.txt
```

Set env vars in backend flask > `docker-compose.yml` 
```yaml
      AWS_DEFAULT_REGION: "${AWS_DEFAULT_REGION}"
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
```

- **Configure LOGGER to use CloudWatch**

add the following code on the `app.py` file in backend-flask after the X-Ray Middleware import:
```python
# Cloudwatch
import watchtower
import logging
from time import strftime
```
Add the code below directly afterwards:
```py
# Configuring Logger to Use CloudWatch
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
LOGGER.addHandler(console_handler)
LOGGER.addHandler(cw_handler)
LOGGER.info('Test log')
```

Modify the imports below:
```sh
from services.home_activities import HomeActivities
from services.show_activity import ShowActivities
```

To log any errors after every request put the code below into `app.py` just before `@app.route("/api/message_groups...")`
```py
# ------- Cloudwatch Logs ----------
@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response
```
The full `app.py` file will be as follows:
```sh

from flask import Flask, request
from flask_cors import CORS, cross_origin
import os
import logging
# Cloudwatch
import watchtower
from time import strftime

# Configuring Logger to Use CloudWatch
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
LOGGER.addHandler(console_handler)
LOGGER.addHandler(cw_handler)
LOGGER.info('Test log')

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

# Import AWS X-Ray SDK
# from aws_xray_sdk.core import xray_recorder
# from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

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

# ------- Cloudwatch Logs ----------
@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response

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

@app.route("/api/activities/notifications", methods=['GET'])
# @xray_recorder.capture('data_notifications')
def data_notifications():
    with tracer.start_as_current_span("data_notifications"):
        data = NotificationsActivities.run()
        return data, 200

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

```
Modify `home_activities.py` as below:
```py
from datetime import datetime, timedelta, timezone
from opentelemetry import trace
import logging

tracer = trace.get_tracer(__name__)
LOGGER = logging.getLogger(__name__)

class HomeActivities:
    @staticmethod
    def run():
        LOGGER.info('Generating mock data for /api/activities/home')

        with tracer.start_as_current_span("home_activities_run"):
            span = trace.get_current_span()
            now = datetime.now(timezone.utc).astimezone()

            results = [
                {
                    'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                    'handle': 'Andrew Brown',
                    'message': 'Cloud is fun!',
                    'created_at': (now - timedelta(days=2)).isoformat(),
                    'expires_at': (now + timedelta(days=5)).isoformat(),
                    'likes_count': 5,
                    'replies_count': 1,
                    'reposts_count': 0,
                    'replies': [
                        {
                            'uuid': '26e12864-1c26-5c3a-9658-97a10f8fea67',
                            'reply_to_activity_uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
                            'handle': 'Worf',
                            'message': 'This post has no honor!',
                            'likes_count': 0,
                            'replies_count': 0,
                            'reposts_count': 0,
                            'created_at': (now - timedelta(days=2)).isoformat()
                        }
                    ],
                },
                {
                    'uuid': '66e12864-8c26-4c3a-9658-95a10f8fea67',
                    'handle': 'Worf',
                    'message': 'I am out of prune juice',
                    'created_at': (now - timedelta(days=7)).isoformat(),
                    'expires_at': (now + timedelta(days=9)).isoformat(),
                    'likes': 0,
                    'replies': []
                },
                {
                    'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
                    'handle': 'Garek',
                    'message': 'My dear doctor, I am just a simple tailor',
                    'created_at': (now - timedelta(hours=1)).isoformat(),
                    'expires_at': (now + timedelta(hours=12)).isoformat(),
                    'likes': 0,
                    'replies': []
                }
            ]

            span.set_attribute("app.result_length", len(results))
            return results

```

Also confirm you have set env vars in `backend flask` > `docker-compose.yml` 
```yaml
      AWS_DEFAULT_REGION: "${AWS_DEFAULT_REGION}"
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
```
Modify `backend-flask/services/user_activities.py` as below:
```py
from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder
class UserActivities:
  def run(user_handle):
    try:
      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()
      
      if user_handle == None or len(user_handle) < 1:
        model['errors'] = ['blank_user_handle']
      else:
        now = datetime.now()
        results = [{
          'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
          'handle':  'Andrew Brown',
          'message': 'Cloud is fun!',
          'created_at': (now - timedelta(days=1)).isoformat(),
          'expires_at': (now + timedelta(days=31)).isoformat()
        }]
        model['data'] = results

      subsegment = xray_recorder.begin_subsegment('mock-data')
      # xray ---
      dict = {
        "now": now.isoformat(),
        "results-size": len(model['data'])
      }
      subsegment.put_metadata('key', dict, 'namespace')
      xray_recorder.end_subsegment()
    finally:  
    #  # Close the segment
      xray_recorder.end_subsegment()
    return model
```

Modify `backend-flask/app.py` to look as below to disable cloudwatch:
```py
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import os

from services.home_activities import *
from services.user_activities import *
from services.create_activity import *
from services.create_reply import *
from services.search_activities import *
from services.message_groups import *
from services.messages import *
from services.create_message import *
from services.show_activity import *

# HoneyComb ---------
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

# X-RAY ----------
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

# CloudWatch Logs ----
import watchtower
import logging

# Rollbar ------
from time import strftime
import os
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception

# Configuring Logger to Use CloudWatch
# LOGGER = logging.getLogger(__name__)
# LOGGER.setLevel(logging.DEBUG)
# console_handler = logging.StreamHandler()
# cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
# LOGGER.addHandler(console_handler)
# LOGGER.addHandler(cw_handler)
# LOGGER.info("test log")

# HoneyComb ---------
# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)

# X-RAY ----------
xray_url = os.getenv("AWS_XRAY_URL")
xray_recorder.configure(service='backend-flask', dynamic_naming=xray_url)

# OTEL ----------
# Show this in the logs within the backend-flask app (STDOUT)
#simple_processor = SimpleSpanProcessor(ConsoleSpanExporter())
#provider.add_span_processor(simple_processor)

trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

app = Flask(__name__)

# X-RAY ----------
XRayMiddleware(app, xray_recorder)

# HoneyComb ---------
# Initialize automatic instrumentation with Flask
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()


frontend = os.getenv('FRONTEND_URL')
backend = os.getenv('BACKEND_URL')
origins = [frontend, backend]
cors = CORS(
  app, 
  resources={r"/api/*": {"origins": origins}},
  expose_headers="location,link",
  allow_headers="content-type,if-modified-since",
  methods="OPTIONS,GET,HEAD,POST"
)

# CloudWatch Logs -----
#@app.after_request
#def after_request(response):
#    timestamp = strftime('[%Y-%b-%d %H:%M]')
#    LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
#    return response

# Rollbar
rollbar_access_token = os.getenv('ROLLBAR_ACCESS_TOKEN')
with app.app_context():
  def init_rollbar():
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

@app.route('/rollbar/test')
def rollbar_test():
    rollbar.report_message('Hello World!', 'warning')
    return "Hello World!"

@app.route("/api/message_groups", methods=['GET'])
def data_message_groups():
  user_handle  = 'andrewbrown'
  model = MessageGroups.run(user_handle=user_handle)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

@app.route("/api/messages/@<string:handle>", methods=['GET'])
def data_messages(handle):
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
@xray_recorder.capture('activities_home')
def data_home():
  data = HomeActivities.run()
  return data, 200

@app.route("/api/activities/@<string:handle>", methods=['GET'])
@xray_recorder.capture('activities_users')
def data_handle(handle):
  model = UserActivities.run(handle)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200

@app.route("/api/activities/search", methods=['GET'])
def data_search():
  term = request.args.get('term')
  model = SearchActivities.run(term)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@app.route("/api/activities", methods=['POST','OPTIONS'])
@cross_origin()
def data_activities():
  user_handle  = 'andrewbrown'
  message = request.json['message']
  ttl = request.json['ttl']
  model = CreateActivity.run(message, user_handle, ttl)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

@app.route("/api/activities/<string:activity_uuid>", methods=['GET'])
@xray_recorder.capture('activities_show')
def data_show_activity(activity_uuid):
  data = ShowActivity.run(activity_uuid=activity_uuid)
  return data, 200

@app.route("/api/activities/<string:activity_uuid>/reply", methods=['POST','OPTIONS'])
@cross_origin()
def data_activities_reply(activity_uuid):
  user_handle  = 'andrewbrown'
  message = request.json['message']
  model = CreateReply.run(message, user_handle, activity_uuid)
  if model['errors'] is not None:
    return model['errors'], 422
  else:
    return model['data'], 200
  return

if __name__ == "__main__":
  app.run(debug=True)
```
At this point X-ray should be working.
Visit the frontend link and append `/@AndrewBrown` to test X-ray
The link will be similar to:
`https://3000-stevecmd-awsbootcampcru-c7fjn6b3pzb.ws-eu107.gitpod.io/@AndrewBrown`
This is similar to pressing the `Home` button on the webpage then clicking on the `logged in users name` in this example its `Andrew Brown`

Cloud watch logs can get expensive, to deactivate them revert the code above as follows:
`home_activities.py`
```py
class HomeActivities:
      def run():
        #logger.info("HomeActivities")
```
and `app.py`
```py
# Configuring Logger to Use CloudWatch
# LOGGER = logging.getLogger(__name__)
# LOGGER.setLevel(logging.DEBUG)
# console_handler = logging.StreamHandler()
# cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
# LOGGER.addHandler(console_handler)
# LOGGER.addHandler(cw_handler)
# LOGGER.info("test log")
```
```py
      @app.route("/api/activities/home", methods=['GET'])
      def data_home():
        data = HomeActivities.run()
        return data, 200
```
We can now disable x-ray as well in `app.py`:
```python
# Xray
# from aws_xray_sdk.core import xray_recorder
# from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
```
```python
# Xray
# xray_url = os.getenv("AWS_XRAY_URL")
# xray_recorder.configure(service='backend-flask', dynamic_naming=xray_url)
```

```python
# xray
# XRayMiddleware(app, xray_recorder)
```

```py
#@app.after_request
#def after_request(response):
#    timestamp = strftime('[%Y-%b-%d %H:%M]')
#    LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
#   return response
```
In `backend-flask` > `services` > `user_activities.py`:
```py
class UserActivities:
  def run(user_handle):
    # xray ---
    #segment = xray_recorder.begin_segment('user_activities')
```
```py
    #subsegment = xray_recorder.begin_subsegment('mock-data')
    # xray ---
    #dict = {
    #  "now": now.isoformat(),
    #  "results-size": len(model['data'])
    #}
    #subsegment.put_metadata('key', dict, 'namespace')

    return model
```
Once done name the commit `Implement cloudwatch logs` and push the changes.

## #4 ROLLBAR
Rollbar is used to **track errors** and monitor applications for error, it tracks and helps one to debug by providing detailed information about the Error.
- **Create your Rollbar account** ->  https://rollbar.com/
- **Then create a new Rollbar Project** : It asks you to setup your project , you get the chance to select your SDK and also provides instructions on how to start.
  Proceed from the Welcome Screen
  Skip 'Add apps'
  On the 'Add SDK' menu' > 'All SDKS' > 'Flask'
- **Access token** is provided for your new Rollbar Project. save it. We will refer to it as <Rollbartoken>
  Skip their installation instructions as they are incomplete for our purposes.

- **Installation** `of blinker` and `rollbar`.
  add these dependencies to 'backend-flask > requirements.txt'
      ```py
      blinker
      rollbar
      ```
  change directories to 'backend-flask' and run:
  ```sh
      pip install -r requirements.txt
  ```
Set the access token as an env var:
```
export ROLLBAR_ACCESS_TOKEN="<Rollbartoken>"
gp env ROLLBAR_ACCESS_TOKEN="<Rollbartoken>"
```
Confirm that the env var has been saved:
```sh
      env | grep ROLLBAR
```
- **Added to backend-flask -> `docker-compose.yml`**
```yaml
ROLLBAR_ACCESS_TOKEN: "${ROLLBAR_ACCESS_TOKEN}"
```
- **Imported** for Rollbar
  insert the following code in -> `backend-flask/app.py` after the cloudwatch logs imports (line 33)
```py
---- Rollbar -----
from time import strftime
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception
```
After the Honeycomb intialization steps ending in:
```py
provider.add_span_processor(processor)
```
add the entry below at around line 95 just above `.../rollbar/test`:
```py
# Rollbar ---------
rollbar_access_token = os.getenv('ROLLBAR_ACCESS_TOKEN')
@app.before_first_request
def init_rollbar():
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
```
- **Add an endpoint to `app.py` to allow rollbar testing:**
  <br>
  Place it just above '@app.route("/api/message_groups'
```py
@app.route('/rollbar/test')
def rollbar_test():
    rollbar.report_message('Hello World!', 'warning')
    return "Hello World!"
```

At this point I wanted to test the notifications endpoint and realized it wasnt working, below are the fixes:


- **Add an endpoint to `app.py` to allow notification:**
  <br>
  Add an import `from services.notifications_activities import *` <br>
  Add the route:
```py
@app.route("/api/activities/notifications", methods=['GET'])
def data_notifications():
  data = NotificationsActivities.run()
  return data, 200
```

Run the app (docker-compose up) to confirm that Rollbar is getting a response.
On the browser, visit the the backend url and append: `.../api/activities/home`
You should see some `json`.

In `docker-compose.yml` under backend-flask > environment, add the Rollbar variables:
```py
      ROLLBAR_ACCESS_TOKEN: "${ROLLBAR_ACCESS_TOKEN}"
```

On the browser, visit the the backend url and append: `.../rollbar/test`
You should get the response:
`Hello World!`
Check the Rollbar website for your logs and make sure to select all the checkboxes under Items > Levels.

### Debugging Rollbar
I was having a hard time getting the docker container to pick up the gitpod env vars. <br />
Solution: <br />
Create a `.env` at the root of the project and store your Rollbar key:
```sh

ROLLBAR_ACCESS_TOKEN = 12345678987654321

```
Remember to block your `.env` file from being pushed to Github by adding the filename `.env` to <br />
the `.gitignore` file.

To confirm that Backend is receiving the key run:
```sh

docker-compose exec backend-flask env | grep ROLLBAR_ACCESS_TOKEN

```

Within `app.py` add the following to get confirmation that Rollbar is working:
```sh

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

```

## [Note] Changes to Rollbar:

During the original bootcamp cohort, there was a newer version of flask.
This resulted in rollback implementation breaking due to a change is the flask api.

If you notice rollbar is not tracking, utilize the code from this file:

`https://github.com/omenking/aws-bootcamp-cruddur-2023/blob/week-x/backend-flask/lib/rollbar.py`

You can test the logs by janking the code eg deleting 'return' at the bottom of the 'home_activities.py' file.
Once you get your responses, make sure to fix the janked code and commit the changes as 'finished implementing rollbar'.

>> Enable Gitpod to auto load ports:

In the `gitpod.yml` file, after the extensions add:
```sh
ports:
  - name: frontend
    port: 3000
    onOpen: open-browser
    visibility: public
  - name: backend
    port: 4567
    visibility: public
  - name: xray-daemon
    port: 2000
    visibility: public
```

<Bold>Enable Gitpod to auto install frontend-react dependencies:</Bold>

In the `gitpod.yml` file, after the `aws-cli` dependency add:
```sh
  - name: react-js
    init: |
      cd frontend-react-js
      npm i
```

<br />

### Demo

To view the endpoints visit ports:
Frontend - port 3000
- Backend - port 4567, <br />
The link will be similar to: `https://4567-stevecmd-awsbootcampcru-c7fjn6b3pzb.ws-eu107.gitpod.io/api/activities/home` to see Home or, 
`https://4567-stevecmd-awsbootcampcru-c7fjn6b3pzb.ws-eu107.gitpod.io/api/activities/notifications` to see the notifications endpoint. 
<br />

- The frontend - port 3000, <br />
The link will be similar to: `https://3000-stevecmd-awsbootcampcru-c7fjn6b3pzb.ws-eu107.gitpod.io/`

### Docker images clean-up
Delete images with <none> tags try either command:
```sh
docker images -q --filter "dangling=true" | xargs docker rmi
docker image prune -f
```
Remove all unused images, not just dangling ones:
```sh
docker image prune -a -f
```
Remove stopped containers:
```sh
docker container prune -f
```
Remove unused volumes:
```sh
docker volume prune -f
```
Remove unused networks:
```sh
docker network prune -f
```
Build and Run Docker Compose:
```sh
docker compose -f "docker-compose.yml" up -d --build
```

![Creating the Honeycomb environment](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Honeycombenvironment.JPG)

## Instrument Honeycomb with OTEL



## Open Telemetry (OTEL) installation
![Installing OTEL](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Installing%20open%20telemetry.JPG)


## Updating App.py to include HoneyComb configuration
![App.py](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/apppy%20update.JPG)


## HoneyComb instrumentation
![HoneyComb instrumentation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Honeycomb%20instrumentation.JPG)


## Setting up the HoneyComb API Key
![HoneyComb API Key](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Honeycomb%20API%20Key%20set.JPG)


## Backend Logs
![Logs from the Backend](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/backend%20view%20logs.JPG)


## Automating of the opening of backend ports
![Automating opening of backend ports](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/ports%20open%20on%20restart.JPG)


## Cruddur returning API endpoint
![API endpoint](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/port%20open%20auto.JPG)

## API endpoint on terminal
![API endpoint](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/api%20endpoint%20sample%201.JPG)


## Successful connection - JSON data
![JSON data](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/backend%20json%20data.JPG)


## Whoami-glitch.me
![WhoAmI](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Honeycomb%20whoami.JPG)


## OTEL configuration
![Configuring OTEL on Gitpod](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/OTEL%20configuration.JPG)


## Working HoneyComb Queries
![Query dashboard on HoneyComb](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/working%20honeycomb.JPG)


## HoneyComb Traces
![Sample recent traces on HoneyComb](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/recent%20traces.JPG)


## HoneyComb Trace Review
![Sample recent traces on HoneyComb](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/review%20trace.JPG)


## Adding a span in homeactivities
![Span creation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/adding%20a%20span.JPG)


## HoneyComb trace of the New Span
![Span Trace](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Recent%20traces%202%20spans.JPG)


## Creating a custom Span
![Custom Span attributes](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/attributes%20for%20custom%20span.JPG)


## Creating a query on HoneyComb
![HoneyComb Query](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/honeycomb%20query.JPG)


## Running Traces on HoneyComb
![HoneyComb Traces](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/traces.JPG)


## Traces report on mock data
![Trace Report](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/specific%20trace.JPG)


## Custom Trace
![Trace Report on mock data](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/trace%20for%20app..JPG)

## New Query
![App result length exists query results](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/new%20query%20using%20app%20result%20length%20exists.JPG)


## Query duration heatmap
![Heatmap of result length exists query](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/heatmap%20of%20duration%20query%20results.JPG)


## Magnifying the Query results
![Magbifying query results](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Magnifying%20results.JPG)

# X-Ray
## Adding X-Ray to requirements
![X-Ray config in requriements](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/xray%20in%20requirements.JPG)

## Additional ports -> x-ray daemon
![Adding additional ports for the x-ray daemon](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Add%20additional%20ports.JPG)

## X-Ray Install
![X-Ray install](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Installing%20x-ray.JPG)

## X-Ray Group ARN on AWS
![X-Ray Group / Permissions on AWS](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/x-ray%20create%20group.JPG)

# RollBar
## Rollbar account creation
![Rollbar Account](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Rollbar%20account%20creation.JPG)

## Selecting Flask as the app type in Rollbar
![Flask selection](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/selecting%20flask%20sdk%20in%20rollbar.JPG)

## Adding Rollbar support - Blinker
![Blinker](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/install%20requirements%20blinker.JPG)

## Creating a Logger on the backend
![Logger for Rollbar](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Logger.JPG)

## Testing access to the Rollbar page
![Rollbar working webpage](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Rollbar%20test.JPG)

## Setting the Rollbar Access token
![Rollbar tokens in backend flask](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Setting%20Rollbar.JPG)

## Setting the Rollbar Access token in Docker 
![Rollbar tokens in Docker compose](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/setting%20rollbar%20access%20token%20in%20docker%20compose.JPG)

## Accessing the test Rollbar webpage 
![Test page - Rollbar](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Rollbar%20test%202.JPG)

## Rollbar Logs Success
![Rollbar Logs](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/rollbar%20success.JPG)

## Rollbar Report
![Rollbar report](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/rollbar%20report.JPG)

## Rollbar Logged occurences
![Logged occurences](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/rollbar%20occurences.JPG)

## Rollbar Error Report
![Rollbar error report](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Error%20logged%20on%20RollBar.JPG)

## Rollbar Error Report Specifics
![Rollbar error report specifics](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%202/Rollbar%20error%20log.JPG)
<hr/>

#### Extra - Automated download branch script
To create and track each remote branch locally one can do it manually by:
```sh

# List all remote branches
git branch -r

# Create a local branch for each remote branch
git checkout -b main origin/main
git checkout -b week-0 origin/week-0
git checkout -b week-1 origin/week-1
git checkout -b week-2 origin/week-2
git checkout -b week-3 origin/week-3
git checkout -b week-4 origin/week-4
git checkout -b week-5 origin/week-5
git checkout -b week-6 origin/week-6
git checkout -b week-7 origin/week-7

```

I automated the process of creating local branches that exist remotely. <br />
`git-branches.sh`:
```sh

# Fetch all branches
git fetch --all

# Loop through each remote branch and create a corresponding local branch
for branch in $(git branch -r | grep -v '\->'); do
    local_branch=${branch#origin/}
    git checkout -b $local_branch $branch
done

```

Make the file executable:
```sh
 chmod u+x git-branches.sh 
```

## Save the work on its own branch named "week-2"
```sh
cd aws-bootcamp-cruddur-2024
git checkout -b week-2
```
<hr/>

## Commit
Add the changes and create a commit named: "Distributed Tracing"
```sh
git add .
git commit -m "Distributed Tracing"
```
Push your changes to the branch
```sh
git push origin week-2
```
<hr/>

### Tag the commit
```sh
git tag -a week-2-tag -m "Setting up Distributed Tracing"
```
<hr/>

### Push your tags
```sh
git push --tags
```
<hr/>

### Switching Between Branches back to Main
```sh
git checkout main
```
<hr/>

### Merge Changes
```sh
git merge week-2
```
<hr/>

### Push Changes to Main
```sh
git push origin main
```
<hr/>

#### Branches?
If you want to keep the "week-1" branch for future reference or additional work, 
you can keep it as is. If you no longer need the branch, you can delete it after merging.
```sh
git branch -d week-2  # Deletes the local branch
git push origin --delete week-2  # Deletes the remote branch
```
