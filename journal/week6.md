# Week 6 — 7 Deploying Serverless Containers
This was technically the seventh week of the Bootcamp. 

(The Hyperlinks in the table below link to the training videos)

**Todo Checklist:**
- [x] [FREE AWS Cloud Project Bootcamp (Week 5) - NoSQL and Caching](https://www.youtube.com/watch?v=5oZHNOaL8Og)
- [x] [ECS Security by Ashish](https://www.youtube.com/watch?v=zz2FQAk1I28&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=57 )
- [x] [Provision ECS Cluster](https://www.youtube.com/watch?v=QIZx2NhdCMI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=58 )
- [x] [Create ECR repo and push image for backend-flask](https://www.youtube.com/watch?v=QIZx2NhdCMI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=58 )
- [x] [Deploy Backend Flask app as a service to Fargate](https://www.youtube.com/watch?v=QIZx2NhdCMI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=58 )
- [x] [Create ECR repo and push image for fronted-react-js](https://www.youtube.com/watch?v=HHmpZ5hqh1I&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=59 )
- [x] [Deploy Frontend React JS app as a service to Fargate](https://www.youtube.com/watch?v=HHmpZ5hqh1I&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=59 )
- [x] [Provision and configure Application Load Balancer along with target groups](https://www.youtube.com/watch?v=HHmpZ5hqh1I&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=59 )
- [x] [Manage your domain useing Route53 via hosted zone](https://www.youtube.com/watch?v=HHmpZ5hqh1I&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=59 )
- [x] [Create an SSL cerificate via ACM](https://www.youtube.com/watch?v=HHmpZ5hqh1I&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=59 )
- [x] [Setup a record set for naked domain to point to frontend-react-js](https://www.youtube.com/watch?v=HHmpZ5hqh1I&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=59 )
- [x] [Setup a record set for api subdomain to point to the backend-flask](https://www.youtube.com/watch?v=HHmpZ5hqh1I&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=59 )
- [x] [Configure CORS to only permit traffic from our domain](https://www.youtube.com/watch?v=HHmpZ5hqh1I&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=59 )
- [x] [Secure Flask by not running in debug mode](https://www.youtube.com/watch?v=9OQZSBKzIgs&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=60 )
- [x] [Implement Refresh Token for Amazon Cognito](https://www.youtube.com/watch?v=LNLP2dxa5EQ&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=63 )
- [x] [Refactor bin directory to be top level](https://www.youtube.com/watch?v=HyJOjBjieb4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=62 )
- [x] [Configure task defintions to contain x-ray and turn on Container Insights](https://www.youtube.com/watch?v=G_8_xtS2MsY&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=64 )
- [x] [Change Docker Compose to explicitly use a user-defined network](https://www.youtube.com/watch?v=G_8_xtS2MsY&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=64 )
- [x] [Create Dockerfile specfically for production use case](https://www.youtube.com/watch?v=G_8_xtS2MsY&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=64 )
- [x] [Using ruby generate out env dot files for docker using erb templates](https://www.youtube.com/watch?v=G_8_xtS2MsY&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=64 )


- [x] Complete 100% of the tasks

<hr/>


|    | Table of contents - Steps taken to complete Week 6 assignments                                                                                                                                                                         |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | [Reinstalling AWS CLI](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#install-aws-cli)                                  |
| 2  | [Healthy targets](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#healthy-target)                                  |
| 3  | [Inspecting docker containers](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#inspecting-docker-container)                                  |
| 4  | [Create ECS cluster](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-ecs-cluster)                                  |
| 5  | [Create Cruddur-python ecr repo](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-cruddur-python-ecr-repo)                                  |
| 6  | [Install session manager plugin](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#install-session-manager-plugin)                                  |
| 7  | [Verify session manager is working](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#verify-session-manager-is-working)                                  |
| 8  | [Login to ECR](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#login-to-ecr)                                  |
| 9  | [Set URL of the Cruddur-python ecr repo created](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#set-url-of-the-cruddur-python-ecr-repo-created)                                  |
| 10 | [Create the Cruddur services Security Group](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-the-cruddur-services-security-group)                                  |
| 11 | [Pull Image of python:3.10-slim-buster](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#pull-image-of-python310-slim-buster)                                  |
| 12 | [Confirm image pulled](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#confirm-image-pulled)                                  |
| 13 | [Tag Image](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#tag-image)                                  |
| 14 | [Push Image to ECR](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#push-image-to-ecr)                                  |
| 15 | [Set URL of backend-flask Repo](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#set-url-of-backend-flask-repo)                                  |
| 16 | [To create ECS task we should create tasks first](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#to-create-ecs-task-we-should-create-tasks-first)                                  |
| 17 | [Create Parameters in parameter store](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-parameters-in-parameter-store)                                  |
| 18 | [Create ExecutionRole then policy](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-executionrole-then-policy)                                  |
| 19 | [Create the service execution policy](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-the-service-execution-policy-then-role-then)                                  |
| 20 | [Register Task Definitions](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#register-task-definitions)                                  |
| 21 | [Confirm parameters have been saved](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#confirm-parameters-have-been-saved)                                  |
| 22 | [Create the taskrole](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-the-taskrole)                                  |
| 23 | [Give the cruddurtaskrole access to cloudwatch](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#give-the-cruddurtaskrole-access-to-cloudwatch)                                  |
| 24 | [Attach a policy to write to the xraydaemon](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#attach-a-policy-to-write-to-the-xraydaemon)                                  |
| 25 | [Create backend task definitions then register](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-backend-task-definitions-then-register)                                  |
| 26 | [Create backend service](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-backend-service)                                  |
| 27 | [Connect to the backend-flask container](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#connect-to-the-backend-flask-container)                                  |
| 28 | [Backend Healthcheck](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#backend-healthcheck)                                  |
| 29 | [Frontend Healthcheck](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#frontend-healthcheck)                                  |
| 30 | [Create a load balancer](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-a-load-balancer)                                  |
| 10 | [Create the frontend task definition: frontend-react-js.json](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-the-frontend-task-definition-frontend-react-jsjson)                                  |
| 10 | [Create front end repo](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-front-end-repo)                                  |
| 10 | [Tag Frontend Image](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#tag-frontend-image)                                  |
| 10 | [Push Frontend image](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#push-frontend-image)                                  |
| 10 | [Part 2](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#part-2)                                  |
| 10 | [Create frontend service if not already running](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-frontend-service-if-not-already-running)                                  |
| 10 | [Build frontend image in prod](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#build-frontend-image-in-prod)                                  |                                                                                                                              
| 10 | [Register Frontend Task Definition](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#register-frontend-task-definition)                                  |
| 10 | [Connecting to the frontend container once running](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#connecting-to-the-frontend-container-once-running)                                  |
| 10 | [Connecting to the backend container once running](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#connecting-to-the-backend-container-once-running)                                  |
| 10 | [Update dockerfile.prod with actual prod input](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#update-dockerfileprod-with-actual-prod-input)                                  |
| 10 | [Working load Balancer](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#working-load-balancer)                                  |
| 10 | [Create the repo for the frontend ECR](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-the-repo-for-the-frontend-ecr)                                  |
| 10 | [Tag the production image](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#tag-the-production-image)                                  |
| 10 | [Implement SSL and configure DNS from the Route 53 console](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#implement-ssl-and-configure-dns-from-the-route-53-console)                                  |
| 10 | [Create records for backend link](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#create-records-for-backend-link)                                  |
| 10 | [Confirm tasks are working](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#confirm-tasks-are-working)                                  |
| 10 | [Confirm services are working](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#confirm-services-are-working)                                  |
| 10 | [Website link is working](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md#website-link-is-working)                                  |
| 10 | []()                                  |
| 10 | []()                                  |
| 10 | []()                                  |
| 10 | []()                                  |
| 10 | []()                                  |
| 10 | []()                                  |
| 10 | []()                                  |
                                                                                                                               

I had previously removed some of the resources so the first step is to redeploy them:
1. Make sure all your environmental requirements are installed:
`pip install -r requirements.txt`
NB: We are not using the RDS Database but one may enable it at the end to confirm everything is working
Run the script located at: `backend-flask/bin/db/test`
Ensure the script is executable by running:
`chmod u+x backend-flask/bin/db/test`

## Install AWS CLI

`curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"`
`unzip awscliv2.zip`
`sudo ./aws/install`

2. Create a health check at app level(app.py)

```@app.route('/api/health-check')
def health_check():
  return {'success': True}, 200
  ```

![Frontend healthcheck](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/Health-check%20container%20level%20frontend.JPG)

Ensure the script is executable by running:
`chmod u+x bin/flask/health-check`
Run the script: `bin/flask/health-check`

![Health check](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/backend%20health%20check%20running.JPG)

3. Create a health check at flask container level
`chmod u+x ./bin/flask/health-check`

![Frontend health check](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/working%20health%20check%20docker%20image.JPG)

## Healthy target
![Check target health in console](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/Healthy%20target.JPG)

## Inspecting Docker container
![Inspect using curl](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/Inspecting%20docker%20container%20locally%20curl.JPG)
![Locally inspect using docker inspect](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/Inspecting%20docker%20container%20locally.JPG)

4. Create cloudwatch log groups:
- App level log group

`aws logs create-log-group --log-group-name "/cruddur"`
`aws logs put-retention-policy --log-group-name "/cruddur" --retention-in-days 1`

![Logs after creation and use of the app](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/backend%20flask%20logs.JPG)

- Fargate container log group
`aws logs create-log-group --log-group-name "/cruddur/fargate-cluster"`
`aws logs put-retention-policy --log-group-name "/cruddur/fargate-cluster" --retention-in-days 1`


## Create ECS cluster
```aws ecs create-cluster \
--cluster-name cruddur \
--service-connect-defaults namespace=cruddur
```

## Create Cruddur-python ecr repo
```aws ecr create-repository \
  --repository-name cruddur-python \
  --image-tag-mutability MUTABLE
  ```

## Install session manager plugin

`curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.deb" -o "session-manager-plugin.deb" `
`sudo dpkg -i session-manager-plugin.deb`

## Verify session manager is working:
`session-manager-plugin`

## Login to ECR

```aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com" ```

After login, we can now push the containers.

## Set URL of the Cruddur-python ecr repo created

`export ECR_PYTHON_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/cruddur-python"`
`echo $ECR_PYTHON_URL`


## Create the Cruddur services Security Group

```export CRUD_SERVICE_SG=$(aws ec2 create-security-group \
  --group-name "crud-srv-sg" \
  --description "Security group for Cruddur services on ECS" \
  --vpc-id $DEFAULT_VPC_ID \
  --query "GroupId" --output text)
echo $CRUD_SERVICE_SG
```

```aws ec2 authorize-security-group-ingress \
  --group-id $CRUD_SERVICE_SG \
  --protocol tcp \
  --port 80 \
  --cidr 0.0.0.0/0
  ```
  
```export CRUD_SERVICE_SG=$(aws ec2 describe-security-groups \
  --filters Name=group-name,Values=crud-srv-sg \
  --query 'SecurityGroups[*].GroupId' \
  --output text)
  ```
  
```aws ec2 authorize-security-group-ingress \
  --group-id $DB_SG_ID \
  --protocol tcp \
  --port 5432 \
  --source-group $CRUD_SERVICE_SG \
  --tag-specifications 'ResourceType=security-group,Tags=[{Key=Name,Value=BACKENDFLASK}]'
  ```

```export DEFAULT_VPC_ID=$(aws ec2 describe-vpcs \
--filters "Name=isDefault, Values=true" \
--query "Vpcs[0].VpcId" \
--output text)
echo $DEFAULT_VPC_ID
```

```export DEFAULT_SUBNET_IDS=$(aws ec2 describe-subnets  \
 --filters Name=vpc-id,Values=$DEFAULT_VPC_ID \
 --query 'Subnets[*].SubnetId' \
 --output json | jq -r 'join(",")')
echo $DEFAULT_SUBNET_IDS
```

Confirm settings:
```echo $AWS_ACCOUNT_ID
export DEFAULT_VPC_ID="vpc-<random id number of your vpc>"
echo $DEFAULT_VPC_ID
```

![Cruudur Services Security group](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/ALB%20security%20group%20crud.srv.sg.JPG)

## Pull Image of python:3.10-slim-buster
`docker pull python:3.10-slim-buster`

## Confirm image pulled
`docker images`

## Tag Image
`docker tag python:3.10-slim-buster $ECR_PYTHON_URL:3.10-slim-buster`

## Push Image to ECR
`docker push $ECR_PYTHON_URL:3.10-slim-buster`

![Compose up db and backend to test setup](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/compose%20up%20db%20and%20backend.JPG)

Or run `docker-compose up backend-flask db`

from the dockerfile of backend-fask change the following line

```FROM python:3.10-slim-buster

  ENV FLASK_ENV=development```

replace your AWS account number below
```FROM <AWS account number>.dkr.ecr.us-east-1.amazonaws.com/cruddur-python:3.10-slim-buster

ENV PORT=4567 ```

Create backend-flask Repo

```aws ecr create-repository \
  --repository-name backend-flask \
  --image-tag-mutability MUTABLE
  ```

## Set URL of backend-flask Repo

`export ECR_BACKEND_FLASK_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/backend-flask"`
`echo $ECR_BACKEND_FLASK_URL`

<bold> Make sure to be in backend-flask directory </bold>
Build Image
`docker build -t backend-flask .`

Tag Image
`docker tag backend-flask:latest $ECR_BACKEND_FLASK_URL:latest`

Push Image
`docker push $ECR_BACKEND_FLASK_URL:latest`

## To create ECS task we should create tasks first
** task role is execution permissions while executionrole are used in execution

## Create Parameters in parameter store
run:
`export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=${HONEYCOMB_API_KEY}"`
`echo $OTEL_EXPORTER_OTLP_HEADERS`

![Confirm on console that parameters were saved](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/Confirm%20saved%20parameters.JPG)

## Create Execution Role then policy
ROLE
```aws iam create-role \    
--role-name CruddurServiceExecutionPolicy  \   
--assume-role-policy-document file://aws/policies/service-assume-role-execution-policy.json
```

POLICY
```aws iam put-role-policy \
  --policy-name CruddurServiceExecutionPolicy \
  --role-name CruddurServiceExecutionRole \
  --policy-document file://aws/policies/service-execution-policy.json
  ```
create the new trust entities in the json file on this path aws/policies/service-assume-role-execution-policy.json
```
{
  "Version":"2012-10-17",
  "Statement":[{
      "Action":["sts:AssumeRole"],
      "Effect":"Allow",
      "Principal":{
        "Service":["ecs-tasks.amazonaws.com"]
    }}]
}
```
Create the service-execution-policy file under the path aws/policies/service-execution-policy.json
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "ssm:GetParameters",
                "ssm:GetParameter"
            ],
            "Resource": "arn:aws:ssm:eu-west-2:238967891447:parameter/cruddur/backend-flask/*"
        }
    ]
}
```

## Create the service execution policy then role then
* replace POLICY_ARN

`aws iam attach-role-policy --policy-arn POLICY_ARN --role-name CruddurServiceExecutionRole`

then

`aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/CloudWatchFullAccess --role-name CruddurTaskRole`
`aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess --role-name CruddurTaskRole`

Confirm on console: Full cloudwatch access to CruddurServiceExecutionRole

## Register Task Definitions
Passing Senstive Data to Task Definition
```aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/AWS_ACCESS_KEY_ID" --value $AWS_ACCESS_KEY_ID
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/AWS_SECRET_ACCESS_KEY" --value $AWS_SECRET_ACCESS_KEY
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/CONNECTION_URL" --value $PROD_CONNECTION_URL
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/ROLLBAR_ACCESS_TOKEN" --value $ROLLBAR_ACCESS_TOKEN
aws ssm put-parameter --type "SecureString" --name "/cruddur/backend-flask/OTEL_EXPORTER_OTLP_HEADERS" --value "x-honeycomb-team=$HONEYCOMB_API_KEY"
```
## Confirm parameters have been saved
![Saved parameters on console ](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/Confirm%20saved%20parameters.JPG)


## Create the taskrole
```aws iam create-role \
    --role-name CruddurTaskRole \
    --assume-role-policy-document "{
  \"Version\":\"2012-10-17\",
  \"Statement\":[{
    \"Action\":[\"sts:AssumeRole\"],
    \"Effect\":\"Allow\",
    \"Principal\":{
      \"Service\":[\"ecs-tasks.amazonaws.com\"]
    }
  }]
}" 
```

attach the SSM access policy
```
aws iam put-role-policy \
  --policy-name SSMAccessPolicy \
  --role-name CruddurTaskRole \
  --policy-document "{
  \"Version\":\"2012-10-17\",
  \"Statement\":[{
    \"Action\":[
      \"ssmmessages:CreateControlChannel\",
      \"ssmmessages:CreateDataChannel\",
      \"ssmmessages:OpenControlChannel\",
      \"ssmmessages:OpenDataChannel\"
    ],
    \"Effect\":\"Allow\",
    \"Resource\":\"*\"
  }]
}
```

![Test SSM connection to frontend](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/ssm%20to%20frontend.JPG)

## Give the cruddurtaskrole access to cloudwatch
`aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/CloudWatchFullAccess --role-name CruddurTaskRole`

## Attach a policy to write to the xraydaemon
`aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess --role-name CruddurTaskRole`

## Create backend task definitions then register: 
`aws ecs register-task-definition --cli-input-json file://aws/task-definitions/backend-flask.json`


*** Edit the default vpc, security group, subnets, in the task definition

## Create backend service
`aws ecs create-service --cli-input-json file://aws/json/service-backend-flask.json`

## Connect to the backend-flask container
*** Session manager must have been installed

## Edit the task number below to connect to the backend flask service
```aws ecs execute-command \
--region $AWS_DEFAULT_REGION \
--cluster cruddur \
--task <task-number> \
--container backend-flask \
--command "/bin/bash" \
--interactive
```

![Connect to Backend flask through SSM](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/succesfull%20connection%20to%20task.JPG)

Ensure to have the following script in your gitpod.yml file
```
    before: |
      cd /workspace
      curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.deb"
      sudo dpkg -i session-manager-plugin.deb
      cd $THEIA_WORKSPACE_ROOT
      cd backend-flask
```

create a new folder ssm at the path /backend-flask/bin/ and create the new file connect-to-backend-flask and connect-to-frontend-react-js and apply execution permissions `chmod u+x` The basic format is as shown below
```
#! /usr/bin/bash

if [ -z "$1" ]; then
    echo "No TASK_ID argument supplied eg ./bin/ecs/connect-to service 291661114f174777aeeaff30522b972d backend-flask"
    exit 1
fi
TASK_ID=$1

if [ -z "$2" ]; then
    echo "No CONTAINER_NAME argument supplied eg ./bin/ecs/connect-to service 291661114f174777aeeaff30522b972d backend-flask"
    exit 2
fi
CONTAINER_NAME=$2


aws ecs execute-command  \
    --region $AWS_DEFAULT_REGION \
    --cluster cruddur \
    --task $TASK_ID \
    --container $CONTAINER_NAME \
    --command "/bin/bash" \
    --interactive
```
![Connect to frontend through created SSM files](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/ssm%20to%20frontend%20ls.JPG)

*check <bold><i>health checks</i></bold>

##  Backend Healthcheck
Run `./bin/flaskhealth-check`

![Healthcheck confirmation backend](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/backend%20health%20check%20running.JPG)

##  Frontend Healthcheck
![Healthcheck confirmation on browser](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/working%20health%20check%20docker%20image.JPG)


# Create a load balancer

add the following code on your service-backend-flask.json

```
    "loadBalancers": [
      {
          "targetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:<AWS Account ID>:targetgroup/cruddur-backend-flask-TG/<random TG ID>",
          "containerName": "backend-flask",
          "containerPort": 4567
      }
    ],
```

## Create the frontend task definition: frontend-react-js.json 
it is under /aws/task-definition

```
{
    "family": "frontend-react-js",
    "executionRoleArn": "arn:aws:iam::<AWS Account ID>:role/CruddurServiceExecutionRole",
    "taskRoleArn": "arn:aws:iam::<AWS Account ID>:role/CruddurTaskRole",
    "networkMode": "awsvpc",
    "cpu": "256",
    "memory": "512",
    "requiresCompatibilities": [ 
      "FARGATE" 
    ],
    "containerDefinitions": [
      {
        "name": "frontend-react-js",
        "image": "<AWS Account ID>.dkr.ecr.us-east-1.amazonaws.com/frontend-react-js:latest",
        "essential": true,
        "healthCheck": {
          "command": [
            "CMD-SHELL",
            "curl -f http://localhost:3000 || exit 1"
          ],
          "interval": 30,
          "timeout": 5,
          "retries": 3
        },
        "portMappings": [
          {
            "containerPort": 3000,
            "protocol": "tcp"
          }
        ],
  
        "logConfiguration": {
          "logDriver": "awslogs",
          "options": {
              "awslogs-group": "cruddur",
              "awslogs-region": "us-east-1",
              "awslogs-stream-prefix": "frontend-react-js"
          }
        }
      }
    ]
  }
```

* create the frontend task definition

` aws ecs register-task-definition --cli-input-json file://aws/task-definitions/frontend-react-js.json `

![register the frontend task definition](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/register%20frontend%20task%20def.JPG)

* Create frontend service
`aws ecs create-service --cli-input-json file://aws/json/service-frontend-react-js.json`

* Create dockerfile.prod in frontend

## Create front end repo
```aws ecr create-repository \
  --repository-name frontend-react-js \
  --image-tag-mutability MUTABLE
  ```

Build backend and map port
```docker build \
--build-arg REACT_APP_BACKEND_URL="http://cruddur-alb-39461277.us-east-1.elb.amazonaws.com:4567" \
--build-arg REACT_APP_AWS_PROJECT_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_COGNITO_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_USER_POOLS_ID="ca-central-1_<unique-number>" \
--build-arg REACT_APP_CLIENT_ID="<unique client ID>" \
-t frontend-react-js \
-f Dockerfile.prod \
.
```

## Tag Frontend Image
`docker tag frontend-react-js:latest $ECR_FRONTEND_REACT_URL:latest`

## Push Frontend image
`docker push $ECR_FRONTEND_REACT_URL:latest`

If you want to run and test it

`docker run --rm -p 3000:3000 -it frontend-react-js`

# Part 2 

## Create frontend service if not already running:

`aws ecs create-service --cli-input-json file://aws/json/service-frontend-react-js.json`

Build frontend image locally - must be in front end react folder
```docker build \
--build-arg REACT_APP_BACKEND_URL="https://4567-$GITPOD_WORKSPACE_ID.$GITPOD_WORKSPACE_CLUSTER_HOST" \
--build-arg REACT_APP_AWS_PROJECT_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_COGNITO_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_USER_POOLS_ID="us-east-1_<unique-number>" \
--build-arg REACT_APP_CLIENT_ID="<unique client ID>" \
-t frontend-react-js \
-f Dockerfile.prod \
.
```
## Build frontend image in prod: 
![build frontend image in prod](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/npm%20run%20build%20on%20frontend.JPG)

If you want to run and test the image locally

`docker ps --to get <container id>`

`docker run --rm -p 3000:3000 -it frontend-react-js`

`docker inspect --to get <container id>`

## Register Frontend Task Definition
`aws ecs register-task-definition --cli-input-json file://aws/task-definitions/frontend-react-js.json`

# Connecting to the frontend container once running: 
`./bin/ecs/connect-to-frontend-react-js <task number>`

# Connecting to the backend container once running: 
![Frontend container connection](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/succesfull%20connection%20to%20task.JPG)

# Update dockerfile.prod with actual prod input
```
# Base Image ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FROM node:16.18 AS build

ARG REACT_APP_BACKEND_URL
ARG REACT_APP_AWS_PROJECT_REGION
ARG REACT_APP_AWS_COGNITO_REGION
ARG REACT_APP_AWS_USER_POOLS_ID
ARG REACT_APP_CLIENT_ID

ENV REACT_APP_BACKEND_URL=$REACT_APP_BACKEND_URL
ENV REACT_APP_AWS_PROJECT_REGION=$REACT_APP_AWS_PROJECT_REGION
ENV REACT_APP_AWS_COGNITO_REGION=$REACT_APP_AWS_COGNITO_REGION
ENV REACT_APP_AWS_USER_POOLS_ID=$REACT_APP_AWS_USER_POOLS_ID
ENV REACT_APP_CLIENT_ID=$REACT_APP_CLIENT_ID

COPY . ./frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
RUN npm run build

![Build the frontend image](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/npm%20run%20build%20on%20frontend.JPG)

# New Base Image ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FROM nginx:1.23.3-alpine

# --from build is coming from the Base Image
COPY --from=build /frontend-react-js/build /usr/share/nginx/html
COPY --from=build /frontend-react-js/nginx.conf /etc/nginx/nginx.conf

EXPOSE 3000
```

create a file called nginx.conf under the frontend-react-js
```
# Set the worker processes
worker_processes 1;

# Set the events module
events {
  worker_connections 1024;
}

# Set the http module
http {
  # Set the MIME types
  include /etc/nginx/mime.types;
  default_type application/octet-stream;

  # Set the log format
  log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

  # Set the access log
  access_log  /var/log/nginx/access.log main;

  # Set the error log
  error_log /var/log/nginx/error.log;

  # Set the server section
  server {
    # Set the listen port
    listen 3000;

    # Set the root directory for the app
    root /usr/share/nginx/html;

    # Set the default file to serve
    index index.html;

    location / {
        # First attempt to serve request as file, then
        # as directory, then fall back to redirecting to index.html
        try_files $uri $uri/ $uri.html /index.html;
    }

    # Set the error page
    error_page  404 /404.html;
    location = /404.html {
      internal;
    }

    # Set the error page for 500 errors
    error_page  500 502 503 504  /50x.html;
    location = /50x.html {
      internal;
    }
  }
}

```

from the folder frontend-react-js run the command to build:

`npm run build`

run the following command to build the image pointing to the local environment:

``` docker build \
--build-arg REACT_APP_BACKEND_URL="https://${CODESPACE_NAME}-4567.${GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN}" \
--build-arg REACT_APP_AWS_PROJECT_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_COGNITO_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_USER_POOLS_ID="$AWS_USER_POOLS_ID" \
--build-arg REACT_APP_CLIENT_ID="$APP_CLIENT_ID" \
-t frontend-react-js \
-f Dockerfile.prod \
.
```

To point to the url of the load balancer:

```
docker build \
--build-arg REACT_APP_BACKEND_URL="http://cruddur-alb-<AWS Account ID>.<AWS_DEFAULT_REGION>.elb.amazonaws.com:4567" \
--build-arg REACT_APP_AWS_PROJECT_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_COGNITO_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_USER_POOLS_ID="$AWS_USER_POOLS_ID" \
--build-arg REACT_APP_CLIENT_ID="$APP_CLIENT_ID" \
-t frontend-react-js \
-f Dockerfile.prod \
.
```
## Working load Balancer

![Working load balancer](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/working%20load%20balancer.JPG)

## Create the repo for the frontend ECR:

``` aws ecr create-repository \
  --repository-name frontend-react-js \
  --image-tag-mutability MUTABLE
```

and set the environment variables:

```export ECR_FRONTEND_REACT_URL="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/frontend-react-js"
echo $ECR_FRONTEND_REACT_URL
```

## Tag the production image:

`docker tag frontend-react-js:latest $ECR_FRONTEND_REACT_URL:latest`

test locally:

`docker run --rm -p 3000:3000 -it frontend-react-js `

push to the repo in ecr:

`docker push $ECR_FRONTEND_REACT_URL:latest`

# Implement SSL and configure DNS from the Route 53 console
* Create a hosted zone
* Update name servers
* Request public certificate under ACM
* At previously created hosted zone, create CNAME records and point them to the load balancer
  `frontend - port 3000`
  `backend - port 4567`

## Create records for backend link 
  ![Create records for backend link](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/Create%20records%20or%20backend%20link.JPG)

In the task definition of the backend, edit the following line:
```
   {"name": "FRONTEND_URL", "value": "https://example.com"},
   {"name": "BACKEND_URL", "value": "https://api.example.com"},
```

once done, relaunch the task definition, recreate the image of the frontend repo and push it.
```
docker build \
--build-arg REACT_APP_BACKEND_URL="https://example.com" \
--build-arg REACT_APP_AWS_PROJECT_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_COGNITO_REGION="$AWS_DEFAULT_REGION" \
--build-arg REACT_APP_AWS_USER_POOLS_ID="$AWS_USER_POOLS_ID" \
--build-arg REACT_APP_CLIENT_ID="$APP_CLIENT_ID" \
-t frontend-react-js \
-f Dockerfile.prod \
.
```
## Confirm tasks are working
![Confirm tasks are working](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/Running%20tasks.JPG)

## Confirm services are working
![Confirm services are working](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/Running%20services.JPG)

## Website link is working
![Link is working](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%206/part%202/New%20link%20is%20up.JPG)