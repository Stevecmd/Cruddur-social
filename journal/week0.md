# Week 0 — Billing and Architecture

## Logical Diagram

Set up accounts on the lucid and come up with the Logical diagram.
![Logical Architectural Diagram](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/Cruddur%20-%20Conceptual%20Diagram.jpeg)
- [Live Logical Diagram as shown above on Lucid chart](https://lucid.app/lucidchart/cd526c7d-0a59-4b3a-b61a-ef5e019293fe/edit?page=0_0&invitationId=inv_5ba96d4e-22e1-4db8-84b5-5fbef5a1739c#)

## Napkin design

Napkin / tissue design method of 
coming up with architecture; drawing out your architecture at a high level but in a way where the conceptual flow makes sense.

![Napkin design](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/Cruddur%20-%20Napkin%20design%20main.JPG)

## Challenges:
Week 0
- Generate credentials,
- AWS CLI setup,
- Create Budget and Billing Alarms via CLI.

Tasks:
- Create the Cruddur Logical Architectural diagram and napkin design.
- Created a Budget to track my spend and put a fixed amount of $10. 
![$10 dollar Budget](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/Budget.JPG)
- Activated the AWS cost allocation tags.
- Investigate costs through cost explorer.
![Cost explorer](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/Cost%20explorer.JPG)

> Note: It cost me $3.48 dollars to buy my domain via Route 53 and an additional $0.50 dollars for Route 53 Hosted zones. 
- Checked out the Free tier services and compared them to the trial services.
- Created a new User with CLI priviledges. <br/>
The user is configured with MFA, Access keys and access policies.
![New User with CLI privilege](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/CLIPriviledgesAccesskey.jpg)
- Configure Gitpod Env vars; <br/>
every time the gitpod environment starts, it will automatically set up a new environment with my 
    preconfigured credentails..
    ![Proof GitPod account](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/Gitpod.JPG)
- Confirmed that the AWS CLI is working and it is indeed displaying the expected user. 
    [Instructions to install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
    ![Proof of aws cli](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/proof%20of%20aws%20cli.JPG)
- Created an AWS Budget via the CLI.
- Enabled Billing and created a billing alarm via CLI.
    ![Proof Billing alarm on the console](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/Budget%20alerts.JPG)

- Created a tag via the CLI.
- Installed aws auto-prompt on the cli
  ![Proof of aws auto-prompt](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%200/aws%20cli%20autoprompt.JPG)

## Getting the AWS CLI Working

### Install AWS CLI

- Install the AWS CLI when our Gitpod enviroment launches.
- Set AWS CLI to use partial autoprompt mode to make it easier to debug CLI commands.
- The bash commands to be used are the same as the [AWS CLI Install Instructions]https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html


Update `.gitpod.yml` to include the following task to auto-install `aws-cli` whenever the environment gets restarted..

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
### Create a new User and Generate AWS Credentials

- Go to (IAM Users Console](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/users) and create a new user.
- `Enable console access` for the user
- Create a new `Admin` Group and apply `AdministratorAccess`
- Create the user and go find and click into the user
- Click on `Security Credentials` and `Create Access Key`
- Choose `AWS CLI Access`.
- Download the CSV with the credentials and save them.

### Set Env Vars

We will set these credentials for the current bash terminal
```
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_DEFAULT_REGION=us-east-1
```

Instructing Gitpod to store these credentials:
```
gp env AWS_ACCESS_KEY_ID=""
gp env AWS_SECRET_ACCESS_KEY=""
gp env AWS_DEFAULT_REGION=us-east-1
```

### Check that the AWS CLI is working and you are the expected user

```sh
aws sts get-caller-identity
```

You should see something like this:
```json
{
    "UserId": "AIDAS4FSKHSZNLYLHDK2B",
    "Account": "197942459570",
    "Arn": "arn:aws:iam::197942459570:user/bc-user"
}
```

## Enable Billing Alerts

- On your AWS Root Account go to the [Billing Page](https://console.aws.amazon.com/billing/)
- Under `Billing Preferences` Choose `Receive Billing Alerts`
- Save Preferences

## Creating a Billing Alarm

### Create SNS Topic

- We need an SNS topic before we create an alarm.
- The SNS topic is what will delivery us an alert when we get overbilled
- [aws sns create-topic](https://docs.aws.amazon.com/cli/latest/reference/sns/create-topic.html)

Create a SNS Topic
```sh
aws sns create-topic --name billing-alarm
```
> Returns a TopicARN

Create a subscription - input the `TopicARN` and your `Email`
```sh
aws sns subscribe \
    --topic-arn TopicARN \
    --protocol email \
    --notification-endpoint your@email.com
```

**Confirm the email subscription.** by visiting your email inbox.

#### Create Alarm

- [aws cloudwatch put-metric-alarm](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/put-metric-alarm.html)
- [Create an Alarm via AWS CLI](https://aws.amazon.com/premiumsupport/knowledge-center/cloudwatch-estimatedcharges-alarm/)
- We need to update the configuration json script with the TopicARN we generated earlier
- We are just a json file because --metrics is is required for expressions and so its easier to use a JSON file.

Create the alarm_config file necessary for the alarm itself `alarm_config.json`:

```
{
    "AlarmName": "DailyEstimatedCharges",
    "AlarmDescription": "This alarm would be triggered if the daily estimated charges exceeds 1$",
    "ActionsEnabled": true,
    "AlarmActions": [
        "arn:aws:sns:us-east-1:XXXXXXXXXX:billing-alarm"
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
Run the alarm:

```sh
aws cloudwatch put-metric-alarm --cli-input-json file://aws/json/alarm_config.json
```

## Create an AWS Budget

[aws budgets create-budget](https://docs.aws.amazon.com/cli/latest/reference/budgets/create-budget.html)

Get your AWS Account ID
```sh
aws sts get-caller-identity --query Account --output text
```

- Supply your AWS Account ID
- Update the json files
- This is another case with AWS CLI its just much easier to json files due to lots of nested json

`budget.json`:
```
{
    "BudgetLimit": {
        "Amount": "10",
        "Unit": "USD"
    },
    "BudgetName": "Example Tag Budget",
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

`budget-notifications-with-subscribers,json`:

```
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
                "Address": "joshhargett.jh@gmail.com",
                "SubscriptionType": "EMAIL"
            }
        ]
    }
  ]
  <sub>This code is for the notifications.</sub>
```
Create the budget:
```sh
aws budgets create-budget \
    --account-id AccountID \
    --budget file://aws/json/budget.json \
    --notifications-with-subscribers file://aws/json/budget-notifications-with-subscribers.json
```

Store `Account id` as an environmental variable:

```
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
gp env AWS_ACCOUNT_ID="XXXXXXXXXXX"
```

We then store the variable in the budget creation code: 

```
aws budgets create-budget \
    --account-id $AWS_ACCOUNT_ID \
    --budget file://aws/json/budget.json \
    --notifications-with-subscribers file://aws/json/budget-notifications-with-subscribers.json
```