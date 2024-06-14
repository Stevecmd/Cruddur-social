# Week 0 — Billing and Architecture

## Challenges:
---
**Todo Checklist:**
- [x] [Watched Week 0 - Live Streamed Video](https://www.youtube.com/watch?v=tDPqmwKMP7Y&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=29)
- [x] [Watched Chirag's Week 0 - Spend Considerations](https://www.youtube.com/watch?v=FKAScachFgk&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=25)
- [x] [Watched Ashish's Week 0 - Security Considerations](https://www.youtube.com/watch?v=zJnNe5Nv4tE&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=22)
- [x] [Recreate Conceptual Diagram in Lucid Charts or on a Napkin](https://www.youtube.com/watch?v=b-idMgFFcpg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=23)
- [x] [Recreate Logical Architectual Diagram in Lucid Charts](https://www.youtube.com/watch?v=OAMHu1NiYoI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=24)
- [x] [Create an Admin User](https://www.youtube.com/watch?v=OdUnNuKylHg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=14)
- [x] Use CloudShell
- [x] Generate AWS Credentials
- [x] Installed AWS CLI
- [x] Create a Billing Alarm
- [x] Create a Budget

- [x] Complete 100% of the tasks

<hr/>

## Tasks:
- Create the Cruddur Logical Architectural diagram and napkin design.
- Create an AWS Organization
- Gitpod
- Getting the AWS CLI Working
- Enable Billing Alerts

### Logical Diagram

Set up accounts on the lucid and come up with the Logical diagram.

![Logical Architectural Diagram](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/Cruddur-Conceptual_Diagram.jpeg)
- [Live Logical Diagram as shown above on Lucid chart](https://lucid.app/lucidchart/cd526c7d-0a59-4b3a-b61a-ef5e019293fe/edit?page=0_0&invitationId=inv_5ba96d4e-22e1-4db8-84b5-5fbef5a1739c#)

### Napkin design

Napkin / tissue design method of 
coming up with architecture; drawing out your architecture at a high level but in a way where the conceptual flow makes sense.

![Napkin design](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/Cruddur-Napkin_design_main.JPG)

- Created a Budget to track my spend and put a fixed amount of $10. 
![$10 dollar Budget](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/Budget.JPG)
- Activated the AWS cost allocation tags.
- Investigate costs through cost explorer.
![Cost explorer](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/Cost_explorer.JPG)

> Note: It cost me $3.48 dollars to buy my domain via Route 53 and an additional $0.50 dollars for Route 53 Hosted zones. 
- Checked out the Free tier services and compared them to the trial services.
- Created a new User with CLI priviledges. <br/>
The user is configured with MFA, Access keys and access policies.
![New User with CLI privilege](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/CLI_Priviledged_Accesskey.jpg)
- Configure Gitpod Env vars; <br/>
every time the gitpod environment starts, it will automatically set up a new environment with my 
    preconfigured credentails..
- Confirmed that the AWS CLI is working and it is indeed displaying the expected user. 
    [Instructions to install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
    ![Proof of aws cli](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/proof_of_aws_cli.JPG)
- Created an AWS Budget via the CLI.
- Enabled Billing and created a billing alarm via CLI.
    ![Proof Billing alarm on the console](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/Budget_alerts.JPG)

- Created a tag via the CLI.
- Installed aws auto-prompt on the cli
  ![Proof of aws auto-prompt](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/aws_cli_autoprompt.JPG)

## Create an AWS Organization
To manage multiple AWS accounts efficiently, start by setting up an AWS Organization. Follow these steps to create and configure your AWS Organization:

1. **Access AWS Organizations**: Navigate to the AWS Console, locate the Services menu, and select AWS Organizations. Click on “Create an Organization” to begin the setup process.

2. **Create Organizational Units**: After your Organization is established, you can create nested Organizational Units (OUs) to group your AWS accounts. To do this, check the box next to the Root Organization, then go to Actions > Organizational Unit > Create New.

![Organizational Structure](https://www.linuxtek.ca/wp-content/uploads/2023/02/Screenshot_2023-02-07_41-26-00.png)

Once the organizational unit is created, you can then create a new account under it. <br />
In order to create multiple accounts using the same email, one may use the format <br />
"example+1@gmail.com" the `+1`, `+2` etc are used to append new account details to the same email. <br />

![Add an Account](https://github.com/Stevecmd/Cruddur-social/blob/week-0/journal/Week%200/Organization/Add%20account.JPG)

![Creating MFA security](https://github.com/Stevecmd/Cruddur-social/blob/week-0/journal/Week%200/Organization/MFA/IAM%202%20MFA%20device.JPG)

![Secure Account with MFA and Access Keys](https://github.com/Stevecmd/Cruddur-social/blob/week-0/journal/Week%200/Organization/MFA/MFA%20and%20Access%20Keys%20Final.JPG)


## Getting the AWS CLI Working

### Install AWS CLI

- To set up the AWS CLI in your Gitpod environment and enable partial autoprompt mode for easier command debugging, follow these steps. The commands are based on the AWS CLI Install Instructions.
- The bash commands to be used are the same as the [AWS CLI Install Instructions]https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

[AWS CLI Installation instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

To install the AWS CLI, you can follow these steps:

1. Download the AWS CLI package from the [AWS website](https://aws.amazon.com/cli/).
```BASH
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```
2. Unzip the package.
```bash
unzip awscliv2.zip
```
3. Run the `install` script.
```bash
sudo ./aws/install
```
4. Verify the installation:
```bash
aws --version
```
> This will print the version of the AWS CLI that is installed.

To set the AWS CLI to use `partial autoprompt mode`, follow these steps:

## **AWS CLI auto-prompt**

The AWS CLI auto-prompt is a feature that allows you to use the `Enter` key to complete commands. <br>
This can save you time and effort when you are using the AWS CLI. <br>
- Enable partial autoprompt mode:
```bash
aws configure set cli_auto_prompt partial
```

To enable the AWS CLI auto-prompt, add the following lines to your `.bashrc` file by running them in the terminal:
```bash

export AWS_CLI_AUTO_PROMPT=on
export PS1="\[\033[38;5;247m\]\u\[$(tput sgr0)\]\[\033[38;5;15m\]@\[$(tput sgr0)\]\[\033[38;5;243m\]\h\[$(tput sgr0)\]\[\033[38;5;15m\]:\[$(tput sgr0)\]\[\033[38;5;47m\]\w\[$(tput sgr0)\]\[\033[38;5;15m\]\\$ \[$(tput sgr0)\]"


```
### Checking AWS Connections with Console

After installing the AWS CLI, you can verify your connection to AWS by running the following command:
```bash
aws sts get-caller-identity
```
This command will return your AWS account ID, AWS Region, and ARN.

To retrieve and store your AWS account ID in an environment variable, use the following command:
```bash
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
```
This command assigns your AWS account ID to the `AWS_ACCOUNT_ID` environment variable, allowing you to use this variable in other AWS CLI commands.


### Gitpod

To enable AWS CLI `auto-prompt` in your Gitpod environment, follow these instructions:

Update your `.gitpod.yml` file to include the following task. This will ensure the `aws-cli` is automatically installed whenever the environment is restarted.

```sh
tasks:
  - name: aws-cli
    env:
      AWS_CLI_AUTO_PROMPT: on-partial
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT
```
This configuration sets up the AWS CLI with auto-prompt mode enabled, making it easier to use CLI commands in your Gitpod environment.
- The bash commands we used are the same as the [AWS CLI Install Instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

### Steps to Create a new User and Generate AWS Credentials

- Navigate to the (IAM Users Console](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/users) and create a new user.
- Enable `console access` for the user
- Create a new `Admin` Group and attach the `AdministratorAccess` policy to it.
- Create the user and then locate and click on the user.
- Click on `Security Credentials` tab and select `Create Access Key`.
- Choose `AWS CLI Access`.
- Download the CSV file containing the credentials and save it securely.

### Set Environment Variables

To set your AWS credentials for the current bash terminal, use the following commands:
```sh
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_DEFAULT_REGION=us-east-1
```

Enable Gitpod to save these credentials for use when we relaunch our workspaces:
```sh
gp env AWS_ACCESS_KEY_ID=""
gp env AWS_SECRET_ACCESS_KEY=""
gp env AWS_DEFAULT_REGION=us-east-1
```
Confirm Gitpod has save these credentials as env vars:
```sh

env | grep AWS_ACCESS_KEY_ID
env | grep AWS_SECRET_ACCESS_KEY
env | grep AWS_DEFAULT_REGION

```
### Verify AWS CLI Functionality and Identity
To check that the AWS CLI is working and confirm your identity, run the following command:
```sh
aws sts get-caller-identity
```

You should see a response similar to this:
```json
{
    "UserId": "AIDAS4FSKHSZNLYLHDK2B",
    "Account": "197942459570",
    "Arn": "arn:aws:iam::197942459570:user/bc-user"
}
```

Store `Account id` as an environmental variable:

```sh
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
gp env AWS_ACCOUNT_ID=XXXXXXXXXXX
```

## Enable Billing Alerts

Turn on Billing Alerts to recieve alerts...

- In your Root Account go to the [Billing Page](https://console.aws.amazon.com/billing/)
- Under `Billing Preferences` Choose `Receive Billing Alerts`
- Save Preferences

<hr/>

### Create SNS Topic

- Before creating the alarm, we need to set up an SNS topic:
- The SNS topic will deliver alerts when there are billing overages.
- Utilize the [aws sns create-topic](https://docs.aws.amazon.com/cli/latest/reference/sns/create-topic.html) command to create the topic.

Create an SNS (Subscriber Notification Service) Topic:
- We need an SNS topic before we create an alarm.
- The SNS topic is what will delivery us an alert when we get overbilled
- [aws sns create-topic](https://docs.aws.amazon.com/cli/latest/reference/sns/create-topic.html)
```sh
aws sns create-topic --name billing-alarm
```
> This command will return a TopicARN.

Then, create a subscription by providing the `TopicARN` and your `Email`:
```sh
aws sns subscribe \
    --topic-arn TopicARN \
    --protocol email \
    --notification-endpoint your@email.com
```

**Confirm the email subscription.** by visiting your email inbox.

### Create an AWS Budget
To create an AWS budget, utilize the
[aws budgets create-budget](https://docs.aws.amazon.com/cli/latest/reference/budgets/create-budget.html) command.

- Create a folder at the top level named aws if it is not already there, in it create a folder named json: 
  ```
  cd Cruddur-social
  mkdir aws
  cd aws
  mkdir json
  cd json
   ```

First, retrieve your AWS Account ID using the following command:
```sh
aws sts get-caller-identity --query Account --output text
```

- Next, update the JSON files `budget.json` and `budget-notifications-with-subscribers.json` as needed.
- Location > `aws/json` :
Create a file named `budget.json` and insert the code below:
```sh
{
    "BudgetLimit": {
        "Amount": "1",
        "Unit": "USD"
    },
    "BudgetName": "One-Dollar-Budget",
    "BudgetType": "COST",
    "CostFilters": {
        "TagKeyValue": [
            "user:Key$value1",
            "user:Key$value2"
        ]
    },
    "CostTypes": {
        "IncludeCredit": true,
        "IncludeDiscount": true,
        "IncludeOtherSubscription": true,
        "IncludeRecurring": true,
        "IncludeRefund": true,
        "IncludeSubscription": true,
        "IncludeSupport": true,
        "IncludeTax": true,
        "IncludeUpfront": true,
        "UseBlended": false
    },
    "TimePeriod": {
        "Start": 1477958399,
        "End": 3706473600
    },
    "TimeUnit": "MONTHLY"
}
```

Create a file named `budget-notifications-with-subscribers.json` and insert the code below:
```sh
[
    {
        "Notification": {
            "ComparisonOperator": "GREATER_THAN",
            "NotificationType": "ACTUAL",
            "Threshold": 80,
            "ThresholdType": "PERCENTAGE"
        },
        "Subscribers": [
            {
                "Address": "<Your email>",
                "SubscriptionType": "EMAIL"
            }
        ]
    }
]
```
Then run the following code in the CLI:

```sh
cd Cruddur-social
```
```sh
aws budgets create-budget \
    --account-id $ACCOUNT_ID \
    --budget file://aws/json/budget.json \
    --notifications-with-subscribers file://aws/json/budget-notifications-with-subscribers.json
```
<hr/>

#### Create Alarm

- To create the alarm, use the [aws cloudwatch put-metric-alarm](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-alarm.html) command.
- [Create an Alarm via AWS CLI](https://aws.amazon.com/premiumsupport/knowledge-center/cloudwatch-estimatedcharges-alarm/)
- We need to update the configuration json script with the TopicARN we generated earlier
- We are just a json file because --metrics is required for expressions and so its easier to use a JSON file.

1. Prepare the `aws/json/alarm_config.json` and insert the following code and also edit the `ACCOUNT_ID` to match your `aws account id`:

```sh
{
    "AlarmName": "DailyEstimatedCharges",
    "AlarmDescription": "This alarm would be triggered if the daily estimated charges exceeds 1$",
    "ActionsEnabled": true,
    "AlarmActions": [
        "arn:aws:sns:us-east-1:<ACCOUNT_ID>:billing-alarm"
    ],
    "EvaluationPeriods": 1,
    "DatapointsToAlarm": 1,
    "Threshold": 1,
    "ComparisonOperator": "GreaterThanOrEqualToThreshold",
    "TreatMissingData": "breaching",
    "Metrics": [{
        "Id": "m1",
        "MetricStat": {
            "Metric": {
                "Namespace": "AWS/Billing",
                "MetricName": "EstimatedCharges",
                "Dimensions": [{
                    "Name": "Currency",
                    "Value": "USD"
                }]
            },
            "Period": 86400,
            "Stat": "Maximum"
        },
        "ReturnData": false
    },
    {
        "Id": "e1",
        "Expression": "IF(RATE(m1)>0,RATE(m1)*86400,0)",
        "Label": "DailyEstimatedCharges",
        "ReturnData": true
    }]
  }
```

2. Deploy the creation of the alarm by running the code below::

```sh
aws cloudwatch put-metric-alarm --cli-input-json file://aws/json/alarm_config.json
```
This setup will create a billing alarm to monitor daily estimated charges and trigger an alert if they exceed $1.

## Add the Backend dependencies to the requirements file
File location:
```sh
backend-flask/requirements.txt
```
Dependencies to be added:
```txt
flask
flask-cors
opentelemetry-api 
opentelemetry-sdk 
opentelemetry-exporter-otlp-proto-http 
opentelemetry-instrumentation-flask 
opentelemetry-instrumentation-requests
aws-xray-sdk
watchtower
blinker
rollbar
```
<hr/>

## Serverless Notification API

A serverless notification API is a sophisticated application leveraging AWS Lambda and Amazon SNS to deliver email notifications to subscribers seamlessly.

- [Setting up Post Notification](#setting-up-post-notification) <br/>
    To initiate the notification system.
1. [Create Lambda](#create-lambda) <br/>
    Begin by crafting a Lambda function capable of processing POST requests containing a name and message payload. The function will then propagate this data to an SNS topic, which in turn dispatches email notifications to subscribed users.
   - [Granting SNS Access to the Lambda Function](#granting-sns-access-to-the-lambda-function) <br />
   Ensure the Lambda function has appropriate permissions to interact with Amazon SNS.
2. [Test Post Endpoint](#test-post-endpoint) <br />
    Verify the functionality of the POST endpoint by sending test requests and confirming the receipt of email notifications by subscribers.

The API works by first creating a Lambda function that accepts POST requests with a name and message. The Lambda function then publishes an SNS message with the name and message to a topic. The SNS topic is configured to send email notifications to subscribers.

The flowchart below illustrates the process intricately:
* An API receives a POST request with a JSON payload containing a `name` and `message`.
* The Lambda function processes the request and extracts the `name` and `message` from the payload.
```yaml
       API Request (POST)       Lambda Function      SNS Topic             Email Subscribers
      +------------------>   +----------------->  +-------------------->  +-----------------+ 
  H   |                      |                    |                    |  | List of EMAILs; | Y
  E   |    {                 |   {                |   {                |  |                 | A
  L   |   "name": "Steve",    |   "name": "Steve",  |   "name": "Steve",  |  |                 | Y
  L   |   "message": "Hey"   |  "message": "Hey"  |   "message": "Hey" |  |      e.g.       | A
  O   |    }                 |   }                |   }                |  |                 | 2
      |                      |                    |                    |  |   Steve Email    | D
  T   +<------------------   +<-----------------  +<-----------------  |  |   Yours, etc.   | E
  H   |    HTTP Response     |    Publish SNS     |    Send Email      |  |                 | V
  E   |                      |    Message         |    Notifications   |  |                 | O
  R   |     Status 200       |    with            |    to Subscribers  |  |                 | P
  E   |                      |    name & message  |                    |  |                 | S
      +----------------------+--------------------+--------------------+  +-----------------+ 
```
* This structured approach ensures seamless communication and reliable delivery of notifications, providing users with timely updates through email.

### Setting up Post Notification

To establish post notifications, follow these steps:

1. Create a new SNS topic and subscribe to it using the provided AWS command:
```bash
aws sns create-topic --name <topic-name>
```
Upon successful creation, note the SNS Topic's Amazon Resource Name (ARN) for future reference. <br/>
Example output:
```bash
{
    "TopicArn": "arn:aws:sns:<region>:<aws-id>:<topic-name>"
}
```
2. Subscribe to the recently created SNS topic using the following AWS command. Replace `<region>` with your AWS region, `<account-id>` with your AWS account ID, and `<email>` with the email address designated for receiving notifications:

```bash
aws sns subscribe \
--topic-arn arn:aws:sns:<region>:<account-id>:<topic-name> \
--protocol email \
--notification-endpoint <email>
```

3. Confirm your subscription to the topic.
![SNS Email subscription confirmation](https://github.com/Stevecmd/Cruddur-social/blob/Documentation/journal/Week%200/SNS%20subscription.JPG)

### Create Lambda

To set up the Lambda function for handling notifications, follow these steps:
1. Create a Lambda function with Python `3.9` runtime.
2. Enable the function URL in the Lambda function configuration 
3. Ensure that authentication is not required for access to the function URL [leave both steps for later.](#assign-url-for-lambda)
3. Use the provided Python code for the Lambda function:

```py
import json
import boto3

def lambda_handler(event, context):
    
    client = boto3.client('sns')
    snsArn = 'arn:aws:sns:<REGION>:<ACCOUNT ID>:<topic-name>'
    
    body = json.loads(event.get("body"))
    
    
    response = client.publish(
        TopicArn = snsArn,
        Message = body.get("message"),
        Subject= f"Hello {body['name']}"
    )
    
    return {
      'statusCode': 200,
      'body': json.dumps(response)
   }
```
4. Assign the SNS ARN to the `sns_arn `variable in the Lambda function code.
5. Deploy the Lambda function.

### **Granting SNS Access to the Lambda Function**

You need to enable SNS access to the Lambda function:

1. Go to the Lambda Function in the AWS Management Console.
2. Click on the **Configuration** tab.
3. In the **Permissions** section, click on the the Role name associated with the Lambda function.
4. Under **Permissions**, click on **Add Permission**.
5. Choose **Attach Policies** to proceed.
6. Filter the policy list and search **AmazonSNSFullAccess**.
7. Select **AmazonSNSFullAccess** and attach it to the Lambda function's role.

### Assign URL for Lambda
Generate an URL for the Lambda function:

1. Open the `configuration pane`.
2. In the left pane, navigate to the `Function URL` section.
3. Generate a new URL and select the `No Authorization` option (`Auth Type; NONE`).
4. Ensure the policy statements have been updated as shown below:
```JSON
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "StatementId": "FunctionURLAllowPublicAccess",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "lambda:InvokeFunctionUrl",
      "Resource": "arn:aws:lambda:<region>:<aws-id>:function:postapi",
      "Condition": {
        "StringEquals": {
          "lambda:FunctionUrlAuthType": "NONE"
        }
      }
    }
  ]
}
```

### Test Post Endpoint

1. Open Thunder Client / PostMan or any other **API testing tool**.

2. Send a POST request to the Lambda function URL with a name and message payload.

3. Use the following curl command as an example: 
```bash
curl --request POST \
  --url     'https://yours.lambda-url.<region>.on.aws/' \
  --header 'Content-Type: application/json' \
  --data '{"name": "SteveJoe", "message": "NOTIFIED: Lambda Post Triggered"}'
```
Replace `https://yours.lambda-url.<region>.on.aws/` with the actual Lambda function URL.

4. Verify that your API tool returns a `200 OK` status on success.

5. Check your subscribed email for the post notification.


## To be done:
> Implement Monitoring: <br/>
Implementing monitoring involves setting up monitoring tools and practices to track the performance and health of your AWS resources. Here's how you can implement monitoring:

1. `Set Up CloudWatch Monitoring`: Configure Amazon CloudWatch to monitor metrics for your AWS resources, such as EC2 instances, RDS databases, and Lambda functions.
2. `Create Custom Metrics`: Create custom CloudWatch metrics to monitor specific application-level metrics that are relevant to your SLAs.
3. `Configure CloudWatch Alarms`: Set up CloudWatch alarms to automatically notify you when predefined thresholds are exceeded for any monitored metric.
4. `Use AWS Trusted Advisor`: Utilize AWS Trusted Advisor to gain insights into your AWS environment and receive recommendations for optimizing performance, security, and cost.
5. `Implement Log Monitoring`: Set up log monitoring using AWS CloudWatch Logs to collect, monitor, and analyze log data from your AWS resources. Use CloudWatch Logs Insights to query and visualize log data for troubleshooting and analysis.

> Cost Allocation Tags: <br/>
Cost allocation tags are key-value pairs that you can assign to AWS resources to categorize and track their costs. Here's how you can implement cost allocation tags:

1. Define Tagging Strategy: Define a tagging strategy that aligns with your organization's cost tracking and reporting requirements. Determine which tags you will use and what information they will represent (e.g., department, project, environment). 

2. Apply Tags to Resources: Apply cost allocation tags to your AWS resources using the AWS Management Console, AWS CLI, or AWS SDKs. Assign appropriate tags to each resource based on your tagging strategy.

3. Enable Cost Allocation Tags: Enable cost allocation tags in the AWS Billing and Cost Management console. Configure cost allocation tags to be included in your AWS Cost Explorer reports and cost allocation reports.

4. Analyze Cost Data: Use AWS Cost Explorer to analyze your AWS costs by tag. Generate cost reports and visualizations to understand cost trends, identify cost drivers, and optimize resource usage.

5. Automate Tagging: Implement automation to ensure consistent and accurate tagging of AWS resources. Use AWS Config rules, AWS Lambda functions, or third-party tools to automatically apply tags based on predefined rules or resource attributes.

## Conclusion
The implementation of best practices outlined in this document demonstrates a comprehensive approach to AWS infrastructure management and DevOps excellence. By incorporating robust monitoring, we ensure the reliability, availability, and performance of our AWS resources, aligning them closely with business objectives. This proactive monitoring not only allows us to meet SLA commitments but also enables us to swiftly identify and address any issues, thereby minimizing downtime and optimizing resource utilization.
<br />

Moreover, the adoption of cost allocation tags exemplifies our commitment to cost optimization and financial accountability. By accurately tagging and tracking costs across our AWS environment, we gain invaluable insights into resource consumption, identify cost drivers, and implement targeted optimization strategies. This meticulous approach to cost management not only safeguards against overspending but also facilitates informed decision-making and resource allocation.
<br />

Together, these practices underscore our expertise in architecting resilient, scalable, and cost-effective solutions on AWS. By adhering to industry best practices and leveraging cutting-edge tools and technologies, we ensure the delivery of high-quality services that meet and exceed customer expectations. As we continue to refine and evolve our practices, we remain steadfast in our pursuit of operational excellence and innovation in the ever-changing landscape of cloud computing.

## Save the work on its own branch named "week-0"
```sh
cd Cruddur-social
git checkout -b week-0
```
<hr/>

## Commit
Add the changes and create a commit named: "Install AWS CLI - update Gitpod tasks"
```sh
git add .
git commit -m "Install AWS CLI - update Gitpod tasks"
```
Push your changes to the branch
```sh
git push origin week-0
```
<hr/>

### Tag the commit
```sh
git tag -a week-0 -m "Setting up project env vars"
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
git merge week-0
```
<hr/>

### Push Changes to Main
```sh
git push origin main
```
<hr/>

#### Branches?
If you want to keep the "week-0" branch for future reference or additional work, 
you can keep it as is. If you no longer need the branch, you can delete it after merging.
```sh
git branch -d week-0  # Deletes the local branch
git push origin --delete week-0  # Deletes the remote branch
```
