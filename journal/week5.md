# Week 5 — DynamoDB and Serverless Caching
This was technically the sixth week of the Bootcamp. 

(The Hyperlinks in the table below link to the training videos)

**Todo Checklist:**
- [x] [FREE AWS Cloud Project Bootcamp (Week 5) - NoSQL and Caching](https://www.youtube.com/watch?v=5oZHNOaL8Og)
- [x] [Week 5 DynamoDb Utility Scripts](https://www.youtube.com/watch?v=pIGi_9E_GwA)
- [x] [Week 5 Implement Conversations with DynamoDB](https://www.youtube.com/watch?v=dWHOsXiAIBU)
- [x] [Week 5 DynamoDB Stream](https://www.youtube.com/watch?v=zGnzM_YdMJU)
- [x] [How to use Amazon DynamoDB for security and speed](https://www.youtube.com/watch?v=gFPljPNnK2Q&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=53)
- [x] [Implement Schema Load Script](https://www.youtube.com/watch?v=pIGi_9E_GwA&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=52)
- [x] [Implement Seed Script](https://www.youtube.com/watch?v=pIGi_9E_GwA&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=52)
- [x] [Implement Scan Script](https://www.youtube.com/watch?v=pIGi_9E_GwA&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=52)
- [x] [Implement Pattern Scripts for Read and List Conversations](https://www.youtube.com/watch?v=pIGi_9E_GwA&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=52)
- [x] [Implement Update Cognito ID Script for Postgres Database](https://www.youtube.com/watch?v=dWHOsXiAIBU&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=54)
- [x] [Implement (Pattern A) Listing Messages in Message Group into Application](https://www.youtube.com/watch?v=dWHOsXiAIBU&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=54)
- [x] [Implement (Pattern B) Listing Messages Group into Application](https://www.youtube.com/watch?v=dWHOsXiAIBU&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=54)
- [x] [Implement (Pattern B) Listing Messages Group into Application](https://www.youtube.com/watch?v=dWHOsXiAIBU&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=54)
- [x] [Implement (Pattern C) Creating a Message for an existing Message Group into Application](https://www.youtube.com/watch?v=dWHOsXiAIBU&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=54)
- [x] [Implement (Pattern D) Creating a Message for a new Message Group into Application](https://www.youtube.com/watch?v=dWHOsXiAIBU&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=54)
- [x] [Implement (Pattern E) Updating a Message Group using DynamoDB Streams](https://www.youtube.com/watch?v=zGnzM_YdMJU&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=55)
- [] Complete 100% of the tasks

<hr/>


|    | Table of contents - Steps taken to complete Week 5 assignments                                                                                                                                                                         |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | [Refactoring my files for better structure](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#refactoring-my-files-for-better-structure)                                |
| 2  | [Updating schema load](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#updating-schema-load)                                                |
| 3  | [Dynamo DB refactor List tables](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#dynamo-db-refactor-list-tables)                                               |
| 4  | [DynamoDB - Schema load](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#dynamodb---schema-load)                                    |
| 5  | [List loaded table via CLI](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#list-loaded-table-via-cli)                                                  |
| 6  | [Create Database](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#create-database)                           |
| 7  | [Schema - load on the DB](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#schema---load-on-the-db)                                              |
| 8  | [Seeding the Database](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#seeding-the-database)                                  |
| 9  | [Dynamo DB seed](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#dynamo-db-seed)                                                     |
| 10 | [Dynamo DB List tables](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#dynamo-db-list-tables)                                  |
| 11 | [Dynamo DB scan operation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#dynamo-db-scan-operation)                                  |
| 12 | [Dynamo DB - get conversation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#dynamo-db---get-conversation)                                  |
| 13 | [Show all users](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#show-all-users)                                  |
| 14 | [Dynamo DB - list conversations](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#dynamo-db---list-conversation)                                  |
| 15 | [Setting up Flask to run on startup](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#setting-up-flask-to-run-on-startup)                                  |
| 16 | [Seeding Dynamo DB](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#seeding-dynamo-db)                                  |
| 17 | [Dynamo DB schema load and list tables](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#dynamo-db-schema-laod-and-list-tables)                                  |
| 18 | [Dynamo DB seed](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#dynamo-db-seed-1)                                  |
| 19 | [Listing registered users from Database](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#listing-registered-users-from-database)                                  |
| 20 | [Listing Cognito registered users](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#listing-registered-users-from-database)                                  |
| 21 | [Testing Database Setup](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#testing-database-setup)                                  |
| 22 | [Confirmation that all scripts are executable](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#confirmation-that-all-scripts-are-executable)                                  |
| 23 | [Activating POSTGres DB and deactivating Production DB (Dynamo DB)](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#activating-postgres-db-and-deactivating-production-db-dynamo-db)                                  |
| 24 | [Running in Developer mode (POSTGres DB)](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#running-in-developer-mode-postgres-db)                                  |
| 25 | [List of registered Cognito User ID's](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#list-of-registered-cognito-user-ids)                                  |
| 26 | [Logging in](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#logging-in)                                  |
| 27 | [Successfull login](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#successfull-login)                                  |
| 28 | [Messages page before seeding data](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#messages-page-before-seeding-data)                                  |
| 29 | [Successfull Cognito UUID update in terminal](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#successfull-cognito-uuid-update-in-terminal)                                  |
| 30 | [Debugging why no messages were showing - Not resolved yet](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#debugging-why-no-messages-were-showing---not-resolved-yet)                                  |
| 31 | [CORS issues](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#cors)                                  |
| 32 | [DynamoDB Streams](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#dynamodb-streams)
| - | [Step 1](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#step-1)                                  |
| - | [Step 2](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#step-2)                                  |
| 33 | [Create endpoint](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#create-endpoint)                                  |
| - | [Create endpoint 2](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#create-endpoint-2)                                  |
| - | [Create endpoint 3](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#create-endpoint-3)                                  |
| - | [Create endpoint - Success](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#create-endpoint---success)                                  |
| 34 | [Load DDB Table](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#load-ddb-table)                                  |
| 35 | [Load Production DDB database](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#load-production-ddb-database)                                  |
| 36 | [Creating the Lambda function](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#creating-the-lambda-function)                                  |
| 37 | [Lambda creation part 2 - Messaging Stream](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#lambda-creation-part-2---messaging-stream)                                  |
| 38 | [Changing the Env vars to use the production environment](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#changing-the-env-vars-to-use-the-production-environment)                                  |
| 39 | [Success at last](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/Final%20Sucess.JPG)                                  |
| 40 | [Imported Conversation data (seed)](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#imported-conversation-data-seed)                                  |
| 41 | [Messages appear on the profile page](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#messages-appear-on-the-profile-page)                                  |
| 42 | [Quick messages highlights on Homepage](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#quick-messages-highlights-on-homepage)                                  |
| 43 | [Message groupings by conversation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#message-groupings-by-conversation)                                  |
| 44 | [Thread of a message](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week5.md#message-thread)                                  |


## Refactoring my files for better structure
![Refactoring my files for better structure](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/Refactoring%20files.JPG)

## Updating schema load
![Updating schema load](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/Updating%20schema-load.JPG)

## Dynamo DB refactor List tables
![Dynamo DB refactor List tables](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/list%20tables.JPG)

## DynamoDB - Schema load
![DynamoDB - Schema load](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/schema%20load.JPG)

## List loaded table via CLI
![List loaded table via CLI](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/list-tables%202.JPG)

## Create Database
![Create Database](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/create%20DB.JPG)

## Schema - load on the DB
![Schema - load on the DB](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/schema%20load%202.JPG)

## Seeding the Database
![Seeding the Database](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/seed.JPG)

## Dynamo DB seed
![Dynamo DB seed](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/ddb%20seed.JPG)

## Dynamo DB List tables
![Dynamo DB List tables](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/list%20tables.JPG)

## Dynamo DB scan operation
![Dynamo DB scan operation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/scan.JPG)

## Dynamo DB - get conversation
![Dynamo DB - get conversation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/get-conversation.JPG)

## Show all users
![Show all users](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DB%20select%20all%20users.JPG)

## Dynamo DB - list conversation
![Dynamo DB - list conversations](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/list%20conversations.JPG)

## Setting up Flask to run on startup
![Setting up Flask to run on startup](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/Adding%20flask%20to%20gitpod%20requirements.JPG)

## Seeding Dynamo DB
![Seeding Dynamo DB](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/seed%20ddb.JPG)

## Dynamo DB schema laod and list tables
![Dynamo DB schema laod and list tables](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/schema%20load%20and%20list%20tables.JPG)

## Dynamo DB seed
![Dynamo DB seed](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/bin%20ddb%20seed.JPG)

## Listing registered users from Database
![Listing registered users from Database](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/showing%20users%20in%20db.JPG)

## Listing Cognito registered users
![Listing Cognito registered users](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/cognito%20list%20users.JPG)

## Testing Database Setup
![Testing Database Setup](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/run%20db%20setup.JPG)

## Confirmation that all scripts are executable
![Confirmation that all scripts are executable](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/all%20scripts%20executable.JPG)

## Activating POSTGres DB and deactivating Production DB (Dynamo DB)
![Activating POSTGres DB and deactivating Production DB (Dynamo DB)](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/activate%20postgres%20disable%20prod.JPG)

## Running in Developer mode (POSTGres DB)
![Running in Developer mode (POSTGres DB)](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/running%20in%20dev%20mode%20now.JPG)

## List of registered Cognito User ID's
![List of registered Cognito User ID's](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/cognito%20user%20ids%20search.JPG)

## Logging in
![Logging in](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/login%20attempt.JPG)

## Successfull login
![Successfull login](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/succesfull%20login.JPG)

## Messages page before seeding data
![Messages page before seeding data](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/messages%20page%20loads.JPG)

## Successfull Cognito UUID update in terminal
![Successfull Cognito UUID update in terminal](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/updated%20cognito%20uuid%20in%20terminal.JPG)

## Debugging why no messages were showing - Not resolved yet
![Debugging why no messages were showing - Not resolved yet](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/chatfix1.JPG)

## CORS!
![The dreaded errors](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/CORS%20errors.JPG)

## DynamoDB Streams
### Step 1
![Step 1](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/Cruddur%20messages.JPG)

### Step 2
![Step 2](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/DynamoDB%20New%20Image.JPG)

## Create endpoint
![Create endpoint 1](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/endopint%201.JPG)

## Create endpoint 2
![Create endpoint 2](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/endpoint%202.JPG)

## Create endpoint 3
![Create endpoint 3](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/endpoint%203.JPG)

## Create endpoint - Success
![Create endpoint - Success](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/endpoint%20success.JPG)

## Load DDB Table
![Load DDB Table](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/load%20DDB%20table.JPG)

## Load Production DDB database
![Load Production DDB database](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/Load%20Prod%20DB.JPG)

## Creating the Lambda function
![Step 1](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/lambda/1.JPG)
![Step 2](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/lambda/2.JPG)
![Step 3](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/lambda/3.JPG)
### Lambda creation part 2 - Messaging Stream
![Homepage](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/lambda/function/1.JPG)
#### Lambda code
![Lambda code](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/lambda/function/2.JPG)
#### Add necessary permissions to role
![Add necessary permissions to role](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/lambda/function/Add%20permissions.JPG)
#### Dynamo DB Production - Schema load
![Dynamo DB Production - Schema load](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/lambda/function/Creating%20Prod%20DDB%20table.JPG)
#### DynamoDB Trigger creation
![DynamoDB Trigger creation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/lambda/function/DDB%20Trigger.JPG)
#### Successfull DynamoDB table creation
![Successfull DynamoDB table creation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/lambda/function/Succesfull%20DDB%20table%20creation.JPG)

## Changing the Env vars to use the production environment
![Changing the Env vars to use the production environment](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/DDB%20streams/Later/Using%20Prod%20env.JPG)

# Week 5 Final fixes and evidence of complete tasks.

### Imported Conversation data (seed)
![Imported Conversation data (seed)](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/Week%205%20fixes/imported%20seed%20data%20conversation.JPG)
### Messages appear on the profile page
![Messages appear on the profile page](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/Week%205%20fixes/message%20appearing%20in%20profile.JPG)
### Quick messages highlights on Homepage
![Quick messages highlights on Homepage](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/Week%205%20fixes/message%20appearing%20in%20Home.JPG)
### Message groupings by conversation
![Message groupings by conversation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/Week%205%20fixes/Message%20appearing%20in%20messages.JPG)
### Message Thread
![Thread of a message](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%205/Week%205%20fixes/Messages%20trail.JPG)

## Data Modelling
A data modelling technique called `single table design` stores all relevant data in a single database table. For the Direct Messaging System in our Cruddur application, we use DynamoDB. <br/>
Four patterns of data access can be distinguished in this context:
`Pattern A` for `displaying message`s (Showing a single conversation). A list of messages that are a part of a message group are visible to users. <br/>
To display message groups, use `Pattern B` (Showing a list of conversations). Users can check the other people they have been communicating with by viewing a list of messaging groups. <br/>
To compose a fresh message in a fresh message group, use `Pattern C` (Create a message). <br/>
To add a new message to an existing message group, use `Pattern D` (update a message_group for the last message).

**Highlights**
`Pattern A`: Shows the messages. Users can see the list of the messages that belong to a message group.
`Pattern B`: Shows the message group conversation with a specific user.
`Pattern C`: Create a new message in a new message group.
`Pattern D`: Create a new message in an exisintg group.

To get started insert the following dependency into `backend-flask` > `requirements.txt`
```
boto3
```
Proceed to install it:
```
pip install -r requirements.txt
```
Set it as a start-up requirements: <br/>
Add a new service under backend-flask in `.gitpod.yml`
```
  - name: flask
    command: |
      cd backend-flask
      pip install -r requirements.txt
```

# Restructure Script Folders
## RDS DB
As we are going to create more scripts, we implement the following folders structure following:
<br/>
For each **postgres script**, the folder will be as follows:
```
backend-flask/bin/db-connect → backend-flask/bin/db/connect
backend-flask/bin/db-create → backend-flask/bin/db/create
backend-flask/bin/db-drop → backend-flask/bin/db/drop
backend-flask/bin/db-schema-load → backend-flask/bin/db/schema-load
backend-flask/bin/db-seed → backend-flask/bin/db/seed
backend-flask/bin/db-sessions → backend-flask/bin/db/sessions
backend-flask/bin/db-setup → backend-flask/bin/db/setup

backend-flask/bin/rds-update-sg-rule → backend-flask/bin/rds/update-sg-rule

```
The structure of `setup` will change as well to accomodate the new names above:
```py
#! /usr/bin/bash
set -e # stop if it fails at any point

CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-setup"
printf "${CYAN}==== ${LABEL}${NO_COLOR}\n"

ABS_PATH=$(readlink -f "$0")
bin_path=$(dirname $ABS_PATH)

source "$bin_path/db/drop"
source "$bin_path/db/create"
source "$bin_path/db/schema-load"
source "$bin_path/db/seed"
python "$bin_path/db/update_cognito_user_ids"
```
Refactor the files in `bin` by placing them in `db` directory, they contain:

**bin/db/connect**:
```
#! /usr/bin/bash

if [ "$1" = "prod" ]; then
  echo "Running in production mode"
  URL=$PROD_CONNECTION_URL
else
  echo "Running in development mode"
  URL=$CONNECTION_URL
fi

psql $URL
```

**bin/db/create**:
```
#! /usr/bin/bash

CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-create"
printf "${CYAN}== ${LABEL}${NO_COLOR}\n"

NO_DB_CONNECTION_URL=$(sed 's/\/cruddur//g' <<<"$CONNECTION_URL")
psql $NO_DB_CONNECTION_URL -c "Create database cruddur;"
```

**bin/db/drop**:
```
#! /usr/bin/bash

CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-drop"
printf "${CYAN}== ${LABEL}${NO_COLOR}\n"

NO_DB_CONNECTION_URL=$(sed 's/\/cruddur//g' <<<"$CONNECTION_URL")
psql $NO_DB_CONNECTION_URL -c "drop database IF EXISTS cruddur;"
```

**bin/db/schema-load**:
```
#! /usr/bin/bash

CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-schema-load"
printf "${CYAN}== ${LABEL}${NO_COLOR}\n"

ABS_PATH=$(readlink -f "$0")
BIN_PATH=$(dirname $ABS_PATH)
PROJECT_PATH=$(dirname $BIN_PATH)
# echo $PROJECT_PATH
BACKEND_FLASK_PATH="$PROJECT_PATH/backend-flask"
# echo "== db-schema-load"
schema_path="$BACKEND_FLASK_PATH/db/schema.sql"
echo $schema_path 

if [ "$1" = "prod" ]; then
  echo "Running in production mode"
  URL=$PROD_CONNECTION_URL
else
  echo "Running in development mode"
  URL=$CONNECTION_URL
fi

psql $URL cruddur < $schema_path
```

**bin/db/seed**:
```
#! /usr/bin/bash

CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-seed"
printf "${CYAN}== ${LABEL}${NO_COLOR}\n"

# echo "== db-schema-load"
# seed_path="$(realpath .)/db/seed.sql"
# echo $seed_path 

ABS_PATH=$(readlink -f "$0")
BIN_PATH=$(dirname $ABS_PATH)
PROJECT_PATH=$(dirname $BIN_PATH)
# echo $PROJECT_PATH
BACKEND_FLASK_PATH="$PROJECT_PATH/backend-flask"
schema_path="$BACKEND_FLASK_PATH/db/schema.sql"
echo $schema_path

if [ "$1" = "prod" ]; then
  echo "Running in production mode"
  CON_URL=$PROD_CONNECTION_URL
else
  echo "Running in development mode"
  CON_URL=$CONNECTION_URL
fi

psql $CON_URL cruddur < $seed_path
```

**bin/db/sessions**:
```
#! /usr/bin/bash
CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-sessions"
printf "${CYAN}== ${LABEL}${NO_COLOR}\n"

if [ "$1" = "prod" ]; then
  echo "Running in production mode"
  URL=$PROD_CONNECTION_URL
else
  echo "Running in development mode"
  URL=$CONNECTION_URL
fi

NO_DB_URL=$(sed 's/\/cruddur//g' <<<"$URL")
psql $NO_DB_URL -c "select pid as process_id, \
       usename as user,  \
       datname as db, \
       client_addr, \
       application_name as app,\
       state \
from pg_stat_activity;"
```

**bin/db/setup**:
```
#! /usr/bin/bash
set -e # stop if it fails at any point

CYAN='\033[1;36m'
NO_COLOR='\033[0m'
LABEL="db-setup"
printf "${CYAN}==== ${LABEL}${NO_COLOR}\n"

ABS_PATH=$(readlink -f "$0")
bin_path=$(dirname $ABS_PATH)

source "$bin_path/db/drop"
source "$bin_path/db/create"
source "$bin_path/db/schema-load"
source "$bin_path/db/seed"
python "$bin_path/db/update_cognito_user_ids"
```

**bin/db/update_cognito_user_ids**:
```
#!/usr/bin/env python3

import boto3
import os
import sys

print("== db-update-cognito-user-ids")
#scripts below are used to import lib.db based on the file structure
current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, '..', '..'))
sys.path.append(parent_path)
from lib.db import db

def update_users_with_cognito_user_id(handle,sub):
  sql = """
    UPDATE public.users
    SET cognito_user_id = %(sub)s
    WHERE
      users.handle = %(handle)s;
  """
  db.query_commit(sql,{ #commiting the data received from 'update_users_with_cognito_user_id'
    'handle' : handle,
    'sub' : sub
  })

def get_cognito_user_ids():
  userpool_id = os.getenv("AWS_COGNITO_USER_POOL_ID")
  client = boto3.client('cognito-idp')
  params = {
    'UserPoolId': userpool_id,
    'AttributesToGet': [
        'preferred_username',
        'sub'
    ]
  }
  response = client.list_users(**params)
  users = response['Users']
  dict_users = {}
  for user in users:
    attrs = user['Attributes']
    sub    = next((a for a in attrs if a["Name"] == 'sub'), None)
    handle = next((a for a in attrs if a["Name"] == 'preferred_username'), None)
    dict_users[handle['Value']] = sub['Value']
  return dict_users

users = get_cognito_user_ids()

for handle, sub in users.items(): #iterating through the data received  to update the list of fields
  print('----',handle,sub)
  update_users_with_cognito_user_id(
    handle=handle,
    sub=sub
  )
```
```sh
chmod u+x bin/db/update_cognito_user_ids
```

**bin/db/test**:
```
#!/usr/bin/env python3
import psycopg
import os
import sys

connection_url = os.getenv("CONNECTION_URL")

conn = None
try:
  print('attempting connection')
  conn = psycopg.connect(connection_url)
  print("Connection successful!")
except psycopg.Error as e:
  print("Unable to connect to the database:", e)
finally:
  conn.close()
```

**bin/db/check-db.sh**:
```
# Check if database already exists
RUN /backend-flask/bin/db/check-db.sh

DB_NAME="cruddur"

# Check if database already exists
if aws rds describe-db-instances --db-instance-identifier "cruddur-db-instance" --query "DBInstances[].DBInstanceIdentifier" --output text | grep -q "cruddur-db-instance"; then
  echo "Database instance already exists. Aborting."
  exit 1
fi
```
Make the file executable:
```
chmod u+x bin/db/check-db.sh 
```

**bin/db/create-rds-db**:
```
# Check if database already exists
RUN /backend-flask/bin/db/check-db.sh

DB_NAME="cruddur"

# Check if database already exists
if aws rds describe-db-instances --db-instance-identifier "cruddur-db-instance" --query "DBInstances[].DBInstanceIdentifier" --output text | grep -q "cruddur-db-instance"; then
  echo "Database instance already exists. Aborting."
  exit 1
fi
```
Make the file executable:
```
chmod u+x bin/db/create-rds-db 
```


## Dynamo DB
First <b>uncomment</b> the DynamoDB env vars in `docker-compose.yml`:
```
  # Dynamo Database configuration ---- Start -----------
  dynamodb-local:
    # https://stackoverflow.com/questions/67533058/persist-local-dynamodb-data-in-volumes-lack-permission-unable-to-open-databa
    # We needed to add user:root to get this working.
    user: root
    command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
    image: "amazon/dynamodb-local:latest"
    container_name: dynamodb-local
    ports:
      - "8000:8000"
    volumes:
      - "./docker/dynamodb:/home/dynamodblocal/data"
    working_dir: /home/dynamodblocal
  # Dynamo Database configuration ---- End -----------
```

Create a new folder: `backend-flask/lib/ddb.py`. <br/>
In it, place the following code:
```py
import boto3
import sys
from datetime import datetime, timedelta, timezone
import uuid
import os
import botocore.exceptions

class Ddb:
  def client():
    endpoint_url = os.getenv("AWS_ENDPOINT_URL")
    if endpoint_url:
      attrs = { 'endpoint_url': endpoint_url }
    else:
      attrs = {}
    dynamodb = boto3.client('dynamodb',**attrs)
    return dynamodb
  def list_message_groups(client,my_user_uuid):
    year = str(datetime.now().year)
    table_name = 'cruddur-messages'
    query_params = {
      'TableName': table_name,
      'KeyConditionExpression': 'pk = :pk AND begins_with(sk,:year)',
      'ScanIndexForward': False,
      'Limit': 20,
      'ExpressionAttributeValues': {
        ':year': {'S': year },
        ':pk': {'S': f"GRP#{my_user_uuid}"}
      }
    }
    print('query-params:',query_params)
    print(query_params)
    # query the table
    response = client.query(**query_params)
    items = response['Items']
    

    results = []
    for item in items:
      last_sent_at = item['sk']['S']
      results.append({
        'uuid': item['message_group_uuid']['S'],
        'display_name': item['user_display_name']['S'],
        'handle': item['user_handle']['S'],
        'message': item['message']['S'],
        'created_at': last_sent_at
      })
    return results
  def list_messages(client,message_group_uuid):
    year = str(datetime.now().year)
    table_name = 'cruddur-messages'
    query_params = {
      'TableName': table_name,
      'KeyConditionExpression': 'pk = :pk AND begins_with(sk,:year)',
      'ScanIndexForward': False,
      'Limit': 20,
      'ExpressionAttributeValues': {
        ':year': {'S': year },
        ':pk': {'S': f"MSG#{message_group_uuid}"}
      }
    }

    response = client.query(**query_params)
    items = response['Items']
    items.reverse()
    results = []
    for item in items:
      created_at = item['sk']['S']
      results.append({
        'uuid': item['message_uuid']['S'],
        'display_name': item['user_display_name']['S'],
        'handle': item['user_handle']['S'],
        'message': item['message']['S'],
        'created_at': created_at
      })
    return results
  def create_message(client,message_group_uuid, message, my_user_uuid, my_user_display_name, my_user_handle):
    now = datetime.now(timezone.utc).astimezone().isoformat()
    created_at = now
    message_uuid = str(uuid.uuid4())

    record = {
      'pk':   {'S': f"MSG#{message_group_uuid}"},
      'sk':   {'S': created_at },
      'message': {'S': message},
      'message_uuid': {'S': message_uuid},
      'user_uuid': {'S': my_user_uuid},
      'user_display_name': {'S': my_user_display_name},
      'user_handle': {'S': my_user_handle}
    }
    # insert the record into the table
    table_name = 'cruddur-messages'
    response = client.put_item(
      TableName=table_name,
      Item=record
    )
    # print the response
    print(response)
    return {
      'message_group_uuid': message_group_uuid,
      'uuid': my_user_uuid,
      'display_name': my_user_display_name,
      'handle':  my_user_handle,
      'message': message,
      'created_at': created_at
    }
  def create_message_group(client, message,my_user_uuid, my_user_display_name, my_user_handle, other_user_uuid, other_user_display_name, other_user_handle):
    print('== create_message_group.1')
    table_name = 'cruddur-messages'

    message_group_uuid = str(uuid.uuid4())
    message_uuid = str(uuid.uuid4())
    now = datetime.now(timezone.utc).astimezone().isoformat()
    last_message_at = now
    created_at = now
    print('== create_message_group.2')

    my_message_group = {
      'pk': {'S': f"GRP#{my_user_uuid}"},
      'sk': {'S': last_message_at},
      'message_group_uuid': {'S': message_group_uuid},
      'message': {'S': message},
      'user_uuid': {'S': other_user_uuid},
      'user_display_name': {'S': other_user_display_name},
      'user_handle':  {'S': other_user_handle}
    }

    print('== create_message_group.3')
    other_message_group = {
      'pk': {'S': f"GRP#{other_user_uuid}"},
      'sk': {'S': last_message_at},
      'message_group_uuid': {'S': message_group_uuid},
      'message': {'S': message},
      'user_uuid': {'S': my_user_uuid},
      'user_display_name': {'S': my_user_display_name},
      'user_handle':  {'S': my_user_handle}
    }

    print('== create_message_group.4')
    message = {
      'pk':   {'S': f"MSG#{message_group_uuid}"},
      'sk':   {'S': created_at },
      'message': {'S': message},
      'message_uuid': {'S': message_uuid},
      'user_uuid': {'S': my_user_uuid},
      'user_display_name': {'S': my_user_display_name},
      'user_handle': {'S': my_user_handle}
    }

    items = {
      table_name: [
        {'PutRequest': {'Item': my_message_group}},
        {'PutRequest': {'Item': other_message_group}},
        {'PutRequest': {'Item': message}}
      ]
    }

    try:
      print('== create_message_group.try')
      # Begin the transaction
      response = client.batch_write_item(RequestItems=items)
      return {
        'message_group_uuid': message_group_uuid
      }
    except botocore.exceptions.ClientError as e:
      print('== create_message_group.error')
      print(e)
```
Create a new folder: `backend-flask/bin/ddb`. <br/>
Create the following files inside ddb: <br/>
**drop**
```
#! /usr/bin/bash

set -e # stop if it fails at any point

if [ -z "$1" ]; then
  echo "No TABLE_NAME argument supplied eg ./bin/ddb/drop cruddur-messages prod "
  exit 1
fi
TABLE_NAME=$1

if [ "$2" = "prod" ]; then
  ENDPOINT_URL=""
else
  ENDPOINT_URL="--endpoint-url=http://localhost:8000"
fi

echo "deleting table: $TABLE_NAME"

aws dynamodb delete-table $ENDPOINT_URL \
  --table-name $TABLE_NAME
```

**list-tables**
```
#! /usr/bin/bash
set -e # stop if it fails at any point

if [ "$1" = "prod" ]; then
    ENDPOINT_URL=""
else
    ENDPOINT_URL="--endpoint-url=http://localhost:8000"
fi

aws dynamodb list-tables $ENDPOINT_URL \
--query TableNames \
--output table
```

**scan**
```
#! /usr/bin/env python3

import boto3
import sys

attrs = {
  'endpoint_url': 'http://localhost:8000'
}
ddb = boto3.resource('dynamodb',**attrs)
table_name = 'cruddur-messages'

table = ddb.Table(table_name)
response = table.scan()

# print ('=======')
# print(response)

items = response['Items']
for item in items:
  print(item)
```

**schema-load**
```
#!/usr/bin/env python3

import boto3
import sys

attrs = {
  'endpoint_url': 'http://localhost:8000'
}

if len(sys.argv) == 2:
  if "prod" in sys.argv[1]:
    attrs = {}

dynamodb = boto3.client('dynamodb',**attrs)

table_name = 'cruddur-messages'

response = dynamodb.create_table(
  TableName=table_name,
  AttributeDefinitions=[
    {
      'AttributeName': 'message_group_uuid',
      'AttributeType': 'S'
    },
    {
      'AttributeName': 'pk',
      'AttributeType': 'S'
    },
    {
      'AttributeName': 'sk',
      'AttributeType': 'S'
    },
  ],
  KeySchema=[
    {
      'AttributeName': 'pk',
      'KeyType': 'HASH'
    },
    {
      'AttributeName': 'sk',
      'KeyType': 'RANGE'
    },
  ],
  GlobalSecondaryIndexes= [{
    'IndexName':'message-group-sk-index',
    'KeySchema':[{
      'AttributeName': 'message_group_uuid',
      'KeyType': 'HASH'
    },{
      'AttributeName': 'sk',
      'KeyType': 'RANGE'
    }],
    'Projection': {
      'ProjectionType': 'ALL'
    },
    'ProvisionedThroughput': {
      'ReadCapacityUnits': 5,
      'WriteCapacityUnits': 5
    },
  }],
  BillingMode='PROVISIONED',
  ProvisionedThroughput={
      'ReadCapacityUnits': 5,
      'WriteCapacityUnits': 5
  }
)

print(response)
```

**seed**
```
#! /usr/bin/env python3

import boto3
import os
import sys
from datetime import datetime, timedelta, timezone
import uuid

current_path = os.path.dirname(os.path.abspath(__file__)) #current path and parent path arebeing used to declare the path of lib.db on line 12
parent_path = os.path.abspath(os.path.join(current_path, '..', '..'))
sys.path.append(parent_path)
from lib.db import db

attrs = {
  'endpoint_url': 'http://localhost:8000'
}
# unset endpoint url for use with production database
if len(sys.argv) == 2:
  if "prod" in sys.argv[1]:
    attrs = {}
ddb = boto3.client('dynamodb',**attrs)

def get_user_uuids():
  sql = """
    SELECT 
      users.uuid,
      users.display_name,
      users.handle
    FROM users
    WHERE
      users.handle IN(
        %(my_handle)s,
        %(other_handle)s
        )
  """
  users = db.query_array_json(sql,{
    'my_handle':  'stevecmd',
    'other_handle': 'andrewbrown'
  })
  my_user    = next((item for item in users if item["handle"] == 'stevecmd'), None)
  other_user = next((item for item in users if item["handle"] == 'andrewbrown'), None)
  results = {
    'my_user': my_user,
    'other_user': other_user
  }
  print('get_user_uuids')
  print(results)
  return(results) #enables us to call the results later in the code

def create_message_group(client,message_group_uuid, my_user_uuid, last_message_at=None, message=None, other_user_uuid=None, other_user_display_name=None, other_user_handle=None):
  table_name = 'cruddur-messages'
  record = {
    'pk':   {'S': f"GRP#{my_user_uuid}"}, #pk is partition key, S signifies these are strings
    'sk':   {'S': last_message_at}, #sk is sort key
    'message_group_uuid': {'S': message_group_uuid},
    'message':  {'S': message},
    'user_uuid': {'S': other_user_uuid},
    'user_display_name': {'S': other_user_display_name},
    'user_handle': {'S': other_user_handle}
  }

  response = client.put_item(
    TableName=table_name,
    Item=record
  )
  print(response)

def create_message(client,message_group_uuid, created_at, message, my_user_uuid, my_user_display_name, my_user_handle):
  record = {
    'pk':   {'S': f"MSG#{message_group_uuid}"},
    'sk':   {'S': created_at },
    'message_uuid': { 'S': str(uuid.uuid4()) },
    'message': {'S': message},
    'user_uuid': {'S': my_user_uuid},
    'user_display_name': {'S': my_user_display_name},
    'user_handle': {'S': my_user_handle}
  }
  # insert the record into the table
  table_name = 'cruddur-messages'
  response = client.put_item(
    TableName=table_name,
    Item=record
  )
  # print the response
  print(response)

message_group_uuid = "5ae290ed-55d1-47a0-bc6d-fe2bc2700399" #str(uuid.uuid4()) - one can generate their own generic UUID here in the given format
now = datetime.now(timezone.utc).astimezone()
users = get_user_uuids()

create_message_group(
  client=ddb,
  message_group_uuid=message_group_uuid,
  my_user_uuid=users['my_user']['uuid'],
  other_user_uuid=users['other_user']['uuid'],
  other_user_handle=users['other_user']['handle'],
  other_user_display_name=users['other_user']['display_name'],
  last_message_at=now.isoformat(),
  message="this is a filler message"
)

# create_message_group(
#   client=ddb,
#   message_group_uuid=message_group_uuid,
#   my_user_uuid=users['other_user']['uuid'],
#   other_user_uuid=users['my_user']['uuid'],
#   other_user_handle=users['my_user']['handle'],
#   other_user_display_name=users['my_user']['display_name'],
#   last_message_at=now.isoformat(),
#   message="this is a filler message"
# )

conversation = """
Person 1: Have you ever watched Babylon 5? It's one of my favorite TV shows!
Person 2: Yes, I have! I love it too. What's your favorite season?
Person 1: I think my favorite season has to be season 3. So many great episodes, like "Severed Dreams" and "War Without End."
Person 2: Yeah, season 3 was amazing! I also loved season 4, especially with the Shadow War heating up and the introduction of the White Star.
Person 1: Agreed, season 4 was really great as well. I was so glad they got to wrap up the storylines with the Shadows and the Vorlons in that season.
Person 2: Definitely. What about your favorite character? Mine is probably Londo Mollari.
Person 1: Londo is great! My favorite character is probably G'Kar. I loved his character development throughout the series.
Person 2: G'Kar was definitely a standout character. I also really liked Delenn's character arc and how she grew throughout the series.
Person 1: Delenn was amazing too, especially with her role in the Minbari Civil War and her relationship with Sheridan. Speaking of which, what did you think of the Sheridan character?
Person 2: I thought Sheridan was a great protagonist. He was a strong leader and had a lot of integrity. And his relationship with Delenn was so well-done.
Person 1: I totally agree! I also really liked the dynamic between Garibaldi and Bester. Those two had some great scenes together.
Person 2: Yes! Their interactions were always so intense and intriguing. And speaking of intense scenes, what did you think of the episode "Intersections in Real Time"?
Person 1: Oh man, that episode was intense. It was so well-done, but I could barely watch it. It was just too much.
Person 2: Yeah, it was definitely hard to watch. But it was also one of the best episodes of the series in my opinion.
Person 1: Absolutely. Babylon 5 had so many great episodes like that. Do you have a favorite standalone episode?
Person 2: Hmm, that's a tough one. I really loved "The Coming of Shadows" in season 2, but "A Voice in the Wilderness" in season 1 was also great. What about you?
Person 1: I think my favorite standalone episode might be "The Long Twilight Struggle" in season 2. It had some great moments with G'Kar and Londo.
Person 2: Yes, "The Long Twilight Struggle" was definitely a standout episode. Babylon 5 really had so many great episodes and moments throughout its run.
Person 1: Definitely. It's a shame it ended after only five seasons, but I'm glad we got the closure we did with the series finale.
Person 2: Yeah, the series finale was really well-done. It tied up a lot of loose ends and left us with a great sense of closure.
Person 1: It really did. Overall, Babylon 5 is just such a great show with fantastic characters, writing, and world-building.
Person 2: Agreed. It's one of my favorite sci-fi shows of all time and I'm always happy to revisit it.
Person 1: Same here. I think one of the things that makes Babylon 5 so special is its emphasis on politics and diplomacy. It's not just a show about space battles and aliens, but about the complex relationships between different species and their political maneuvering.
Person 2: Yes, that's definitely one of the show's strengths. And it's not just about big-picture politics, but also about personal relationships and the choices characters make.
Person 1: Exactly. I love how Babylon 5 explores themes of redemption, forgiveness, and sacrifice. Characters like G'Kar and Londo have such compelling arcs that are driven by their choices and actions.
Person 2: Yes, the character development in Babylon 5 is really top-notch. Even minor characters like Vir and Franklin get their moments to shine and grow over the course of the series.
Person 1: I couldn't agree more. And the way the show handles its themes is so nuanced and thought-provoking. For example, the idea of "the one" and how it's used by different characters in different ways.
Person 2: Yes, that's a really interesting theme to explore. And it's not just a one-dimensional concept, but something that's explored in different contexts and with different characters.
Person 1: And the show also does a great job of balancing humor and drama. There are so many funny moments in the show, but it never detracts from the serious themes and the high stakes.
Person 2: Absolutely. The humor is always organic and never feels forced. And the show isn't afraid to go dark when it needs to, like in "Intersections in Real Time" or the episode "Sleeping in Light."
Person 1: Yeah, those episodes are definitely tough to watch, but they're also some of the most powerful and memorable episodes of the series. And it's not just the writing that's great, but also the acting and the production values.
Person 2: Yes, the acting is fantastic across the board. From Bruce Boxleitner's performance as Sheridan to Peter Jurasik's portrayal of Londo, every actor brings their A-game. And the production design and special effects are really impressive for a TV show from the 90s.
Person 1: Definitely. Babylon 5 was really ahead of its time in terms of its visuals and special effects. And the fact that it was all done on a TV budget makes it even more impressive.
Person 2: Yeah, it's amazing what they were able to accomplish with the limited resources they had. It just goes to show how talented the people behind the show were.
Person 1: Agreed. It's no wonder that Babylon 5 has such a devoted fanbase, even all these years later. It's just such a well-crafted and timeless show.
Person 2: Absolutely. I'm glad we can still appreciate it and talk about it all these years later. It really is a show that stands the test of time.
Person 1: One thing I really appreciate about Babylon 5 is how it handles diversity and representation. It has a really diverse cast of characters from different species and backgrounds, and it doesn't shy away from exploring issues of prejudice and discrimination.
Person 2: Yes, that's a great point. The show was really ahead of its time in terms of its diverse cast and the way it tackled issues of race, gender, and sexuality. And it did so in a way that felt natural and integrated into the story.
Person 1: Definitely. It's great to see a show that's not afraid to tackle these issues head-on and address them in a thoughtful and nuanced way. And it's not just about representation, but also about exploring different cultures and ways of life.
Person 2: Yes, the show does a great job of world-building and creating distinct cultures for each of the species. And it's not just about their physical appearance, but also about their customs, beliefs, and values.
Person 1: Absolutely. It's one of the things that sets Babylon 5 apart from other sci-fi shows. The attention to detail and the thought that went into creating this universe is really impressive.
Person 2: And it's not just the aliens that are well-developed, but also the human characters. The show explores the different factions and political ideologies within EarthGov, as well as the different cultures and traditions on Earth.
Person 1: Yes, that's another great aspect of the show. It's not just about the conflicts between different species, but also about the internal struggles within humanity. And it's all tied together by the overarching plot of the Shadow War and the fate of the galaxy.
Person 2: Definitely. The show does a great job of balancing the episodic stories with the larger arc, so that every episode feels important and contributes to the overall narrative.
Person 1: And the show is also great at building up tension and suspense. The slow burn of the Shadow War and the mystery of the Vorlons and the Shadows kept me on the edge of my seat throughout the series.
Person 2: Yes, the show is really good at building up anticipation and delivering satisfying payoffs. Whether it's the resolution of a character arc or the climax of a season-long plotline, Babylon 5 always delivers.
Person 1: Agreed. It's just such a well-crafted and satisfying show, with so many memorable moments and characters. I'm really glad we got to talk about it today.
Person 2: Me too. It's always great to geek out about Babylon 5 with someone who appreciates it as much as I do!
Person 1: Yeah, it's always fun to discuss our favorite moments and characters from the show. And there are so many great moments to choose from!
Person 2: Definitely. I think one of the most memorable moments for me was the "goodbye" scene between G'Kar and Londo in the episode "Objects at Rest." It was such a poignant and emotional moment, and it really showed how far their characters had come.
Person 1: Yes, that was a really powerful scene. It was great to see these two former enemies come together and find common ground. And it was a great way to wrap up their character arcs.
Person 2: Another memorable moment for me was the speech that Sheridan gives in "Severed Dreams." It's such an iconic moment in the show, and it really encapsulates the themes of the series.
Person 1: Yes, that speech is definitely one of the highlights of the series. It's so well-written and well-delivered, and it really captures the sense of hope and defiance that the show is all about.
Person 2: And speaking of great speeches, what did you think of the "Ivanova is always right" speech from "Moments of Transition"?
Person 1: Oh man, that speech gives me chills every time I watch it. It's such a powerful moment for Ivanova, and it really shows her strength and determination as a leader.
Person 2: Yes, that speech is definitely a standout moment for Ivanova's character. And it's just one example of the great writing and character development in the show.
Person 1: Absolutely. It's a testament to the talent of the writers and actors that they were able to create such rich and complex characters with so much depth and nuance.
Person 2: And it's not just the main characters that are well-developed, but also the supporting characters like Marcus, Zack, and Lyta. They all have their own stories and struggles, and they all contribute to the larger narrative in meaningful ways.
Person 1: Definitely. Babylon 5 is just such a well-rounded and satisfying show in every way. It's no wonder that it's still beloved by fans all these years later.
Person 2: Agreed. It's a show that has stood the test of time, and it will always hold a special place in my heart as one of my favorite TV shows of all time.
Person 1: One of the most interesting ethical dilemmas presented in Babylon 5 is the treatment of the Narn by the Centauri. What do you think about that storyline?
Person 2: Yeah, it's definitely a difficult issue to grapple with. On the one hand, the Centauri were portrayed as the aggressors, and their treatment of the Narn was brutal and unjust. But on the other hand, the show also presented some nuance to the situation, with characters like Londo and Vir struggling with their own complicity in the conflict.
Person 1: Exactly. I think one of the strengths of the show is its willingness to explore complex ethical issues like this. It's not just about good guys versus bad guys, but about the shades of grey in between.
Person 2: Yeah, and it raises interesting questions about power and oppression. The Centauri had more advanced technology and military might than the Narn, which allowed them to dominate and subjugate the Narn people. But at the same time, there were also political and economic factors at play that contributed to the conflict.
Person 1: And it's not just about the actions of the Centauri government, but also about the actions of individual characters. Londo, for example, was initially portrayed as a somewhat sympathetic character, but as the series progressed, we saw how his choices and actions contributed to the suffering of the Narn people.
Person 2: Yes, and that raises interesting questions about personal responsibility and accountability. Can an individual be held responsible for the actions of their government or their society? And if so, to what extent?
Person 1: That's a really good point. And it's also interesting to consider the role of empathy and compassion in situations like this. Characters like G'Kar and Delenn showed compassion towards the Narn people and fought against their oppression, while others like Londo and Cartagia were more indifferent or even sadistic in their treatment of the Narn.
Person 2: Yeah, and that raises the question of whether empathy and compassion are innate traits, or whether they can be cultivated through education and exposure to different cultures and perspectives.
Person 1: Definitely. And it's also worth considering the role of forgiveness and reconciliation. The Narn and Centauri eventually came to a sort of reconciliation in the aftermath of the Shadow War, but it was a difficult and painful process that required a lot of sacrifice and forgiveness on both sides.
Person 2: Yes, and that raises the question of whether forgiveness is always possible or appropriate in situations of oppression and injustice. Can the victims of such oppression ever truly forgive their oppressors, or is that too much to ask?
Person 1: It's a tough question to answer. I think the show presents a hopeful message in the end, with characters like G'Kar and Londo finding a measure of redemption and reconciliation. But it's also clear that the scars of the conflict run deep and that healing takes time and effort.
Person 2: Yeah, that's a good point. Ultimately, I think the show's treatment of the Narn-Centauri conflict raises more questions than it answers, which is a testament to its complexity and nuance. It's a difficult issue to grapple with, but one that's worth exploring and discussing.
Person 1: Let's switch gears a bit and talk about the character of Natasha Alexander. What did you think about her role in the series?
Person 2: I thought Natasha Alexander was a really interesting character. She was a tough and competent security officer, but she also had a vulnerable side and a complicated past.
Person 1: Yeah, I agree. I think she added a lot of depth to the show and was a great foil to characters like Garibaldi and Zack.
Person 2: And I also appreciated the way the show handled her relationship with Garibaldi. It was clear that they had a history and a lot of unresolved tension, but the show never made it too melodramatic or over-the-top.
Person 1: That's a good point. I think the show did a good job of balancing the personal drama with the larger political and sci-fi elements. And it was refreshing to see a female character who was just as tough and competent as the male characters.
Person 2: Definitely. I think Natasha Alexander was a great example of a well-written and well-rounded female character. She wasn't just there to be eye candy or a love interest, but had her own story and agency.
Person 1: However, I did feel like the show could have done more with her character. She was introduced fairly late in the series, and didn't have as much screen time as some of the other characters.
Person 2: That's true. I think the show had a lot of characters to juggle, and sometimes that meant some characters got sidelined or didn't get as much development as they deserved.
Person 1: And I also thought that her storyline with Garibaldi could have been developed a bit more. They had a lot of history and tension between them, but it felt like it was resolved too quickly and neatly.
Person 2: I can see where you're coming from, but I also appreciated the way the show didn't drag out the drama unnecessarily. It was clear that they both had feelings for each other, but they also had to focus on their jobs and the larger conflicts at play.
Person 1: I can see that perspective as well. Overall, I think Natasha Alexander was a great addition to the show and added a lot of value to the series. It's a shame we didn't get to see more of her.
Person 2: Agreed. But at least the show was able to give her a satisfying arc and resolution in the end. And that's a testament to the show's strength as a whole.
Person 1: One thing that really stands out about Babylon 5 is the quality of the special effects. What did you think about the show's use of CGI and other visual effects?
Person 2: I thought the special effects in Babylon 5 were really impressive, especially for a show that aired in the 90s. The use of CGI to create the spaceships and other sci-fi elements was really innovative for its time.
Person 1: Yes, I was really blown away by the level of detail and realism in the effects. The ships looked so sleek and futuristic, and the space battles were really intense and exciting.
Person 2: And I also appreciated the way the show integrated the visual effects with the live-action footage. It never felt like the effects were taking over or overshadowing the characters or the story.
Person 1: Absolutely. The show had a great balance of practical effects and CGI, which helped to ground the sci-fi elements in a more tangible and realistic world.
Person 2: And it's also worth noting the way the show's use of visual effects evolved over the course of the series. The effects in the first season were a bit rough around the edges, but by the end of the series, they had really refined and perfected the look and feel of the show.
Person 1: Yes, I agree. And it's impressive how they were able to accomplish all of this on a TV budget. The fact that the show was able to create such a rich and immersive sci-fi universe with limited resources is a testament to the talent and creativity of the production team.
Person 2: Definitely. And it's one of the reasons why the show has aged so well. Even today, the visual effects still hold up and look impressive, which is a rarity for a show that's almost 30 years old.
Person 1: Agreed. And it's also worth noting the way the show's use of visual effects influenced other sci-fi shows that came after it. Babylon 5 really set the bar for what was possible in terms of sci-fi visuals on TV.
Person 2: Yes, it definitely had a big impact on the genre as a whole. And it's a great example of how innovative and groundbreaking sci-fi can be when it's done right.
Person 1: Another character I wanted to discuss is Zathras. What did you think of his character?
Person 2: Zathras was a really unique and memorable character. He was quirky and eccentric, but also had a lot of heart and sincerity.
Person 1: Yes, I thought he was a great addition to the show. He added some much-needed comic relief, but also had some important moments of character development.
Person 2: And I appreciated the way the show used him as a sort of plot device, with his knowledge of time and space being instrumental in the resolution of some of the show's major storylines.
Person 1: Definitely. It was a great way to integrate a seemingly minor character into the larger narrative. And it was also interesting to see the different versions of Zathras from different points in time.
Person 2: Yeah, that was a clever storytelling device that really added to the sci-fi elements of the show. And it was also a great showcase for actor Tim Choate, who played the character with so much charm and energy.
Person 1: I also thought that Zathras was a great example of the show's commitment to creating memorable and unique characters. Even characters that only appeared in a few episodes, like Zathras or Bester, were given distinct personalities and backstories.
Person 2: Yes, that's a good point. Babylon 5 was really great at creating a diverse and interesting cast of characters, with each one feeling like a fully-realized and distinct individual.
Person 1: And Zathras was just one example of that. He was a small but important part of the show's legacy, and he's still remembered fondly by fans today.
Person 2: Definitely. I think his character is a great example of the show's ability to balance humor and heart, and to create memorable and beloved characters that fans will cherish for years to come.
"""

lines = conversation.lstrip('\n').rstrip('\n').split('\n') #Breaks out the dummy conversation into an array with each line as a cell and also splits each new line
for i in range(len(lines)): #iterating through the dummy conversation
  if lines[i].startswith('Person 1: '):
    key = 'my_user' #Person 1
    message = lines[i].replace('Person 1: ', '')
  elif lines[i].startswith('Person 2: '):
    key = 'other_user' #Person 2
    message = lines[i].replace('Person 2: ', '')
  else:
    print(lines[i])
    raise 'invalid line' # Good practice to catch errors
  
  # created_at = (now + timedelta(minutes=i)).isoformat()
  created_at = (now + timedelta(hours=-3) + timedelta(minutes=i)).isoformat()
  
  create_message(
    client=ddb,
    message_group_uuid=message_group_uuid,
    created_at=created_at,
    message=message,
    my_user_uuid=users[key]['uuid'],
    my_user_display_name=users[key]['display_name'],
    my_user_handle=users[key]['handle']
  )
```


There are three types of items to insert in the Dynamo DB Table:
```
my_message_group = {
    'pk': {'S': f"GRP#{my_user_uuid}"},
    'sk': {'S': last_message_at},
    'message_group_uuid': {'S': message_group_uuid},
    'message': {'S': message},
    'user_uuid': {'S': other_user_uuid},
    'user_display_name': {'S': other_user_display_name},
    'user_handle':  {'S': other_user_handle}
}

other_message_group = {
    'pk': {'S': f"GRP#{other_user_uuid}"},
    'sk': {'S': last_message_at},
    'message_group_uuid': {'S': message_group_uuid},
    'message': {'S': message},
    'user_uuid': {'S': my_user_uuid},
    'user_display_name': {'S': my_user_display_name},
    'user_handle':  {'S': my_user_handle}
}

message = {
    'pk':   {'S': f"MSG#{message_group_uuid}"},
    'sk':   {'S': created_at},
    'message': {'S': message},
    'message_uuid': {'S': message_uuid},
    'user_uuid': {'S': my_user_uuid},
    'user_display_name': {'S': my_user_display_name},
    'user_handle': {'S': my_user_handle}
}
```
Create the following folders and files inside ddb: <br/>
Folder `patterns` create the following files:
**get-conversation**
```
#!/usr/bin/env python3

import boto3
import sys
import json
import datetime

attrs = {
  'endpoint_url': 'http://localhost:8000'
}

if len(sys.argv) == 2:
  if "prod" in sys.argv[1]:
    attrs = {}

dynamodb = boto3.client('dynamodb',**attrs)
table_name = 'cruddur-messages'

message_group_uuid = "5ae290ed-55d1-47a0-bc6d-fe2bc2700399"

year = str(datetime.datetime.now().year)
# define the query parameters
query_params = {
  'TableName': table_name,
  'ScanIndexForward': False,
  'Limit': 20,
  'ReturnConsumedCapacity': 'TOTAL',
  'KeyConditionExpression': 'pk = :pk AND begins_with(sk,:year)',
  #'KeyConditionExpression': 'pk = :pk AND sk BETWEEN :start_date AND :end_date',
  'ExpressionAttributeValues': {
    ':year': {'S': year },
    #":start_date": { "S": "2023-03-01T00:00:00.000000+00:00" },
    #":end_date": { "S": "2023-03-19T23:59:59.999999+00:00" },
    ':pk': {'S': f"MSG#{message_group_uuid}"}
  }
}


# query the table
response = dynamodb.query(**query_params)

# print the items returned by the query
print(json.dumps(response, sort_keys=True, indent=2))

# print the consumed capacity
print(json.dumps(response['ConsumedCapacity'], sort_keys=True, indent=2))

items = response['Items']
items.reverse()

for item in reversed_array:
  sender_handle = item['user_handle']['S']
  message       = item['message']['S']
  timestamp     = item['sk']['S']
  dt_object = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')
  formatted_datetime = dt_object.strftime('%Y-%m-%d %I:%M %p')
  print(f'{sender_handle: <12}{formatted_datetime: <22}{message[:40]}...')
```

**list-conversations**
```py
#!/usr/bin/env python3

import boto3
import sys
import json
import os

current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, '..', '..', '..'))
sys.path.append(parent_path)
from lib.db import db

attrs = {
  'endpoint_url': 'http://localhost:8000'
}

if len(sys.argv) == 2:
  if "prod" in sys.argv[1]:
    attrs = {}

dynamodb = boto3.client('dynamodb',**attrs)
table_name = 'cruddur-messages'

def get_my_user_uuid():
  sql = """
    SELECT 
      users.uuid
    FROM users
    WHERE
      users.handle =%(handle)s
  """
  uuid = db.query_value(sql,{
    'handle':  'andrewbrown'
  })
  return uuid

my_user_uuid = get_my_user_uuid()
print(f"my-uuid: {my_user_uuid}")
year = str(datetime.now().year)
# define the query parameters
query_params = {
  'TableName': table_name,
  'KeyConditionExpression': 'pk = :pk AND begins_with(sk,:year)',
  'ScanIndexForward': False,
  'ExpressionAttributeValues': {
    ':year': {'S': year },
    ':pk': {'S': f"GRP#{my_user_uuid}"}
  },
  'ReturnConsumedCapacity': 'TOTAL'
}

# query the table
response = dynamodb.query(**query_params)

# print the items returned by the query
print(json.dumps(response, sort_keys=True, indent=2))
```
Create the folder `backend-flask/bin/cognito` and in it create the following files:
list-users
```
#!/usr/bin/env python3

import boto3
import os
import json

userpool_id = os.getenv("AWS_COGNITO_USER_POOL_ID")
client = boto3.client('cognito-idp')
params = {
  'UserPoolId': userpool_id,
  'AttributesToGet': [
      'preferred_username',
      'sub'
  ]
}
response = client.list_users(**params)
users = response['Users']

print(json.dumps(users, sort_keys=True, indent=2, default=str))

dict_users = {}
for user in users:
  attrs = user['Attributes']
  sub    = next((a for a in attrs if a["Name"] == 'sub'), None)
  handle = next((a for a in attrs if a["Name"] == 'preferred_username'), None)
  dict_users[handle['Value']] = sub['Value']

print(json.dumps(dict_users, sort_keys=True, indent=2, default=str))
```

Run `docker compose up` and confirm that Dynamo DB is running. <br/>

While in `backend-flask` - Make our files executable:
```
chmod u+x bin/ddb/drop
chmod u+x bin/ddb/list-tables
chmod u+x bin/ddb/scan
chmod u+x bin/ddb/schema-load
chmod u+x bin/ddb/seed
```
Test the scripts while in `backend-flask`: <br/>
If the table exists, the command below will show that the schema has been loaded.
```
./bin/ddb/schema-load
```
The command below will show the existing tables.
```
./bin/ddb/list-tables
```
The command below will input data in our table.
```
./bin/ddb/seed
```
The command below will scan the existing data in the table.
```
./bin/ddb/scan
```
**NB**  <br/>
Only use `drop` if you want to delete a table:<br/>
`./bin/ddb/drop cruddur-messages prod`

Run: <br/>
`./bin/db/create` - To create a database. <br/>
`./bin/db/schema-load` - To load our schema to the database.<br/>
`./bin/db/seed` - To load our data to the database.<br/>
## Working of Backend 
I had to restructure the BASH Scripts with 3 folders having the Utility Commands for PSQL `backend-flask/bin/db`;  DynamoDB `backend-flask/bin/db`; AWS RDS `backend-flask/bin/rds` and AWS Cognito `backend-flask/bin/cognito`. <br/>
In order to create, configure, and administer AWS services like DynamoDB, add `boto3` to `backend-flask/requirements.txt`.<br/>
As noted in this change, add a command that will enable gitpod to automatically install Python libraries whenever a new workspace is launched.

**In Postgres Local Database**
Adding 3 users and 1 action to the seed data in `backend-flask/db/seed.sql`: <br/>
**NB** Make sure to edit `('<YourName>', '<yourmailid>', '<youruserhandle>' ,'MOCK')`. <br/>
For example: `('Londo Mollari','lmollari@centari.com' ,'londo' ,'MOCK')` <br/>
```
-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('<YourName>', '<yourmailid>', '<youruserhandle>' ,'MOCK'),
  ('Andrew Bayko','bayko@exampro.co' , 'bayko' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = '<youruserhandle>' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )
  ```
To list `users` data saved in AWS Cognito, create the backend-flask/bin/cognito/list-users script.
```
#!/usr/bin/env python3

import boto3
import os
import json

userpool_id = os.getenv("AWS_COGNITO_USER_POOL_ID")
client = boto3.client('cognito-idp')
params = {
    'UserPoolId': userpool_id,
    'AttributesToGet': [
        'preferred_username',
        'sub'
    ]
}
response = client.list_users(**params)
users = response['Users']

print(json.dumps(users, sort_keys=True, indent=2, default=str))

dict_users = {}
for user in users:
    attrs = user['Attributes']
    sub = next((a for a in attrs if a["Name"] == 'sub'), None)
    handle = next(
        (a for a in attrs if a["Name"] == 'preferred_username'), None)
    dict_users[handle['Value']] = sub['Value']

print(dict_users)
```
Note: Inside the file **backend-flask/bin/db/setup** we added the following code:

```
python "$bin_path/db/update_cognito_user_ids"
```
To update users in the seed data with actual Cognito IDs, if any, create the `backend-flask/bin/db/update_cognito_user_ids` script.
```
#!/usr/bin/env python3

import boto3
import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, '..', '..'))
sys.path.append(parent_path)
from lib.db import db

def update_users_with_cognito_user_id(handle, sub):
    sql = """
    UPDATE public.users
    SET cognito_user_id = %(sub)s
    WHERE
      users.handle = %(handle)s;
  """
    db.query_commit(sql, {
        'handle': handle,
        'sub': sub
    })


def get_cognito_user_ids():
    userpool_id = os.getenv("AWS_COGNITO_USER_POOL_ID")
    client = boto3.client('cognito-idp')
    params = {
        'UserPoolId': userpool_id,
        'AttributesToGet': [
            'preferred_username',
            'sub'
        ]
    }
    response = client.list_users(**params)
    users = response['Users']
    dict_users = {}
    for user in users:
        attrs = user['Attributes']
        sub = next((a for a in attrs if a["Name"] == 'sub'), None)
        handle = next(
            (a for a in attrs if a["Name"] == 'preferred_username'), None)
        dict_users[handle['Value']] = sub['Value']
    return dict_users


users = get_cognito_user_ids()

for handle, sub in users.items():
    print('----', handle, sub)
    update_users_with_cognito_user_id(
        handle=handle,
        sub=sub
    )
```

Add a conversation between the user and a user handle named 'bayko' in `seed.sql` file under `bin/ddb` folder. Note the time metric it is actually works:

```
create_message_group(
  client=ddb,
  message_group_uuid=message_group_uuid,
  my_user_uuid=users['other_user']['uuid'],
  other_user_uuid=users['my_user']['uuid'],
  other_user_handle=users['my_user']['handle'],
  other_user_display_name=users['my_user']['display_name'],
  last_message_at=now.isoformat(),
  message="this is a filler message"
)

conversation = """
Person 1: Have you ever watched Babylon 5? It's one of my favorite TV shows!
Person 2: Yes, I have! I love it too. What's your favorite season?
Person 1: I think my favorite season has to be season 3. So many great episodes, like "Severed Dreams" and "War Without End."
Person 2: Yeah, season 3 was amazing! I also loved season 4, especially with the Shadow War heating up and the introduction of the White Star.
Person 1: Agreed, season 4 was really great as well. I was so glad they got to wrap up the storylines with the Shadows and the Vorlons in that season.
Person 2: Definitely. What about your favorite character? Mine is probably Londo Mollari.
Person 1: Londo is great! My favorite character is probably G'Kar. I loved his character development throughout the series.
Person 2: G'Kar was definitely a standout character. I also really liked Delenn's character arc and how she grew throughout the series.
Person 1: Delenn was amazing too, especially with her role in the Minbari Civil War and her relationship with Sheridan. Speaking of which, what did you think of the Sheridan character?
Person 2: I thought Sheridan was a great protagonist. He was a strong leader and had a lot of integrity. And his relationship with Delenn was so well-done.
Person 1: I totally agree! I also really liked the dynamic between Garibaldi and Bester. Those two had some great scenes together.
Person 2: Yes! Their interactions were always so intense and intriguing. And speaking of intense scenes, what did you think of the episode "Intersections in Real Time"?
Person 1: Oh man, that episode was intense. It was so well-done, but I could barely watch it. It was just too much.
Person 2: Yeah, it was definitely hard to watch. But it was also one of the best episodes of the series in my opinion.
Person 1: Absolutely. Babylon 5 had so many great episodes like that. Do you have a favorite standalone episode?
Person 2: Hmm, that's a tough one. I really loved "The Coming of Shadows" in season 2, but "A Voice in the Wilderness" in season 1 was also great. What about you?
Person 1: I think my favorite standalone episode might be "The Long Twilight Struggle" in season 2. It had some great moments with G'Kar and Londo.
Person 2: Yes, "The Long Twilight Struggle" was definitely a standout episode. Babylon 5 really had so many great episodes and moments throughout its run.
Person 1: Definitely. It's a shame it ended after only five seasons, but I'm glad we got the closure we did with the series finale.
Person 2: Yeah, the series finale was really well-done. It tied up a lot of loose ends and left us with a great sense of closure.
Person 1: It really did. Overall, Babylon 5 is just such a great show with fantastic characters, writing, and world-building.
Person 2: Agreed. It's one of my favorite sci-fi shows of all time and I'm always happy to revisit it.
Person 1: Same here. I think one of the things that makes Babylon 5 so special is its emphasis on politics and diplomacy. It's not just a show about space battles and aliens, but about the complex relationships between different species and their political maneuvering.
Person 2: Yes, that's definitely one of the show's strengths. And it's not just about big-picture politics, but also about personal relationships and the choices characters make.
Person 1: Exactly. I love how Babylon 5 explores themes of redemption, forgiveness, and sacrifice. Characters like G'Kar and Londo have such compelling arcs that are driven by their choices and actions.
Person 2: Yes, the character development in Babylon 5 is really top-notch. Even minor characters like Vir and Franklin get their moments to shine and grow over the course of the series.
Person 1: I couldn't agree more. And the way the show handles its themes is so nuanced and thought-provoking. For example, the idea of "the one" and how it's used by different characters in different ways.
Person 2: Yes, that's a really interesting theme to explore. And it's not just a one-dimensional concept, but something that's explored in different contexts and with different characters.
Person 1: And the show also does a great job of balancing humor and drama. There are so many funny moments in the show, but it never detracts from the serious themes and the high stakes.
Person 2: Absolutely. The humor is always organic and never feels forced. And the show isn't afraid to go dark when it needs to, like in "Intersections in Real Time" or the episode "Sleeping in Light."
Person 1: Yeah, those episodes are definitely tough to watch, but they're also some of the most powerful and memorable episodes of the series. And it's not just the writing that's great, but also the acting and the production values.
Person 2: Yes, the acting is fantastic across the board. From Bruce Boxleitner's performance as Sheridan to Peter Jurasik's portrayal of Londo, every actor brings their A-game. And the production design and special effects are really impressive for a TV show from the 90s.
Person 1: Definitely. Babylon 5 was really ahead of its time in terms of its visuals and special effects. And the fact that it was all done on a TV budget makes it even more impressive.
Person 2: Yeah, it's amazing what they were able to accomplish with the limited resources they had. It just goes to show how talented the people behind the show were.
Person 1: Agreed. It's no wonder that Babylon 5 has such a devoted fanbase, even all these years later. It's just such a well-crafted and timeless show.
Person 2: Absolutely. I'm glad we can still appreciate it and talk about it all these years later. It really is a show that stands the test of time.
Person 1: One thing I really appreciate about Babylon 5 is how it handles diversity and representation. It has a really diverse cast of characters from different species and backgrounds, and it doesn't shy away from exploring issues of prejudice and discrimination.
Person 2: Yes, that's a great point. The show was really ahead of its time in terms of its diverse cast and the way it tackled issues of race, gender, and sexuality. And it did so in a way that felt natural and integrated into the story.
Person 1: Definitely. It's great to see a show that's not afraid to tackle these issues head-on and address them in a thoughtful and nuanced way. And it's not just about representation, but also about exploring different cultures and ways of life.
Person 2: Yes, the show does a great job of world-building and creating distinct cultures for each of the species. And it's not just about their physical appearance, but also about their customs, beliefs, and values.
Person 1: Absolutely. It's one of the things that sets Babylon 5 apart from other sci-fi shows. The attention to detail and the thought that went into creating this universe is really impressive.
Person 2: And it's not just the aliens that are well-developed, but also the human characters. The show explores the different factions and political ideologies within EarthGov, as well as the different cultures and traditions on Earth.
Person 1: Yes, that's another great aspect of the show. It's not just about the conflicts between different species, but also about the internal struggles within humanity. And it's all tied together by the overarching plot of the Shadow War and the fate of the galaxy.
Person 2: Definitely. The show does a great job of balancing the episodic stories with the larger arc, so that every episode feels important and contributes to the overall narrative.
Person 1: And the show is also great at building up tension and suspense. The slow burn of the Shadow War and the mystery of the Vorlons and the Shadows kept me on the edge of my seat throughout the series.
Person 2: Yes, the show is really good at building up anticipation and delivering satisfying payoffs. Whether it's the resolution of a character arc or the climax of a season-long plotline, Babylon 5 always delivers.
Person 1: Agreed. It's just such a well-crafted and satisfying show, with so many memorable moments and characters. I'm really glad we got to talk about it today.
Person 2: Me too. It's always great to geek out about Babylon 5 with someone who appreciates it as much as I do!
Person 1: Yeah, it's always fun to discuss our favorite moments and characters from the show. And there are so many great moments to choose from!
Person 2: Definitely. I think one of the most memorable moments for me was the "goodbye" scene between G'Kar and Londo in the episode "Objects at Rest." It was such a poignant and emotional moment, and it really showed how far their characters had come.
Person 1: Yes, that was a really powerful scene. It was great to see these two former enemies come together and find common ground. And it was a great way to wrap up their character arcs.
Person 2: Another memorable moment for me was the speech that Sheridan gives in "Severed Dreams." It's such an iconic moment in the show, and it really encapsulates the themes of the series.
Person 1: Yes, that speech is definitely one of the highlights of the series. It's so well-written and well-delivered, and it really captures the sense of hope and defiance that the show is all about.
Person 2: And speaking of great speeches, what did you think of the "Ivanova is always right" speech from "Moments of Transition"?
Person 1: Oh man, that speech gives me chills every time I watch it. It's such a powerful moment for Ivanova, and it really shows her strength and determination as a leader.
Person 2: Yes, that speech is definitely a standout moment for Ivanova's character. And it's just one example of the great writing and character development in the show.
Person 1: Absolutely. It's a testament to the talent of the writers and actors that they were able to create such rich and complex characters with so much depth and nuance.
Person 2: And it's not just the main characters that are well-developed, but also the supporting characters like Marcus, Zack, and Lyta. They all have their own stories and struggles, and they all contribute to the larger narrative in meaningful ways.
Person 1: Definitely. Babylon 5 is just such a well-rounded and satisfying show in every way. It's no wonder that it's still beloved by fans all these years later.
Person 2: Agreed. It's a show that has stood the test of time, and it will always hold a special place in my heart as one of my favorite TV shows of all time.
Person 1: One of the most interesting ethical dilemmas presented in Babylon 5 is the treatment of the Narn by the Centauri. What do you think about that storyline?
Person 2: Yeah, it's definitely a difficult issue to grapple with. On the one hand, the Centauri were portrayed as the aggressors, and their treatment of the Narn was brutal and unjust. But on the other hand, the show also presented some nuance to the situation, with characters like Londo and Vir struggling with their own complicity in the conflict.
Person 1: Exactly. I think one of the strengths of the show is its willingness to explore complex ethical issues like this. It's not just about good guys versus bad guys, but about the shades of grey in between.
Person 2: Yeah, and it raises interesting questions about power and oppression. The Centauri had more advanced technology and military might than the Narn, which allowed them to dominate and subjugate the Narn people. But at the same time, there were also political and economic factors at play that contributed to the conflict.
Person 1: And it's not just about the actions of the Centauri government, but also about the actions of individual characters. Londo, for example, was initially portrayed as a somewhat sympathetic character, but as the series progressed, we saw how his choices and actions contributed to the suffering of the Narn people.
Person 2: Yes, and that raises interesting questions about personal responsibility and accountability. Can an individual be held responsible for the actions of their government or their society? And if so, to what extent?
Person 1: That's a really good point. And it's also interesting to consider the role of empathy and compassion in situations like this. Characters like G'Kar and Delenn showed compassion towards the Narn people and fought against their oppression, while others like Londo and Cartagia were more indifferent or even sadistic in their treatment of the Narn.
Person 2: Yeah, and that raises the question of whether empathy and compassion are innate traits, or whether they can be cultivated through education and exposure to different cultures and perspectives.
Person 1: Definitely. And it's also worth considering the role of forgiveness and reconciliation. The Narn and Centauri eventually came to a sort of reconciliation in the aftermath of the Shadow War, but it was a difficult and painful process that required a lot of sacrifice and forgiveness on both sides.
Person 2: Yes, and that raises the question of whether forgiveness is always possible or appropriate in situations of oppression and injustice. Can the victims of such oppression ever truly forgive their oppressors, or is that too much to ask?
Person 1: It's a tough question to answer. I think the show presents a hopeful message in the end, with characters like G'Kar and Londo finding a measure of redemption and reconciliation. But it's also clear that the scars of the conflict run deep and that healing takes time and effort.
Person 2: Yeah, that's a good point. Ultimately, I think the show's treatment of the Narn-Centauri conflict raises more questions than it answers, which is a testament to its complexity and nuance. It's a difficult issue to grapple with, but one that's worth exploring and discussing.
Person 1: Let's switch gears a bit and talk about the character of Natasha Alexander. What did you think about her role in the series?
Person 2: I thought Natasha Alexander was a really interesting character. She was a tough and competent security officer, but she also had a vulnerable side and a complicated past.
Person 1: Yeah, I agree. I think she added a lot of depth to the show and was a great foil to characters like Garibaldi and Zack.
Person 2: And I also appreciated the way the show handled her relationship with Garibaldi. It was clear that they had a history and a lot of unresolved tension, but the show never made it too melodramatic or over-the-top.
Person 1: That's a good point. I think the show did a good job of balancing the personal drama with the larger political and sci-fi elements. And it was refreshing to see a female character who was just as tough and competent as the male characters.
Person 2: Definitely. I think Natasha Alexander was a great example of a well-written and well-rounded female character. She wasn't just there to be eye candy or a love interest, but had her own story and agency.
Person 1: However, I did feel like the show could have done more with her character. She was introduced fairly late in the series, and didn't have as much screen time as some of the other characters.
Person 2: That's true. I think the show had a lot of characters to juggle, and sometimes that meant some characters got sidelined or didn't get as much development as they deserved.
Person 1: And I also thought that her storyline with Garibaldi could have been developed a bit more. They had a lot of history and tension between them, but it felt like it was resolved too quickly and neatly.
Person 2: I can see where you're coming from, but I also appreciated the way the show didn't drag out the drama unnecessarily. It was clear that they both had feelings for each other, but they also had to focus on their jobs and the larger conflicts at play.
Person 1: I can see that perspective as well. Overall, I think Natasha Alexander was a great addition to the show and added a lot of value to the series. It's a shame we didn't get to see more of her.
Person 2: Agreed. But at least the show was able to give her a satisfying arc and resolution in the end. And that's a testament to the show's strength as a whole.
Person 1: One thing that really stands out about Babylon 5 is the quality of the special effects. What did you think about the show's use of CGI and other visual effects?
Person 2: I thought the special effects in Babylon 5 were really impressive, especially for a show that aired in the 90s. The use of CGI to create the spaceships and other sci-fi elements was really innovative for its time.
Person 1: Yes, I was really blown away by the level of detail and realism in the effects. The ships looked so sleek and futuristic, and the space battles were really intense and exciting.
Person 2: And I also appreciated the way the show integrated the visual effects with the live-action footage. It never felt like the effects were taking over or overshadowing the characters or the story.
Person 1: Absolutely. The show had a great balance of practical effects and CGI, which helped to ground the sci-fi elements in a more tangible and realistic world.
Person 2: And it's also worth noting the way the show's use of visual effects evolved over the course of the series. The effects in the first season were a bit rough around the edges, but by the end of the series, they had really refined and perfected the look and feel of the show.
Person 1: Yes, I agree. And it's impressive how they were able to accomplish all of this on a TV budget. The fact that the show was able to create such a rich and immersive sci-fi universe with limited resources is a testament to the talent and creativity of the production team.
Person 2: Definitely. And it's one of the reasons why the show has aged so well. Even today, the visual effects still hold up and look impressive, which is a rarity for a show that's almost 30 years old.
Person 1: Agreed. And it's also worth noting the way the show's use of visual effects influenced other sci-fi shows that came after it. Babylon 5 really set the bar for what was possible in terms of sci-fi visuals on TV.
Person 2: Yes, it definitely had a big impact on the genre as a whole. And it's a great example of how innovative and groundbreaking sci-fi can be when it's done right.
Person 1: Another character I wanted to discuss is Zathras. What did you think of his character?
Person 2: Zathras was a really unique and memorable character. He was quirky and eccentric, but also had a lot of heart and sincerity.
Person 1: Yes, I thought he was a great addition to the show. He added some much-needed comic relief, but also had some important moments of character development.
Person 2: And I appreciated the way the show used him as a sort of plot device, with his knowledge of time and space being instrumental in the resolution of some of the show's major storylines.
Person 1: Definitely. It was a great way to integrate a seemingly minor character into the larger narrative. And it was also interesting to see the different versions of Zathras from different points in time.
Person 2: Yeah, that was a clever storytelling device that really added to the sci-fi elements of the show. And it was also a great showcase for actor Tim Choate, who played the character with so much charm and energy.
Person 1: I also thought that Zathras was a great example of the show's commitment to creating memorable and unique characters. Even characters that only appeared in a few episodes, like Zathras or Bester, were given distinct personalities and backstories.
Person 2: Yes, that's a good point. Babylon 5 was really great at creating a diverse and interesting cast of characters, with each one feeling like a fully-realized and distinct individual.
Person 1: And Zathras was just one example of that. He was a small but important part of the show's legacy, and he's still remembered fondly by fans today.
Person 2: Definitely. I think his character is a great example of the show's ability to balance humor and heart, and to create memorable and beloved characters that fans will cherish for years to come.
"""


lines = conversation.lstrip('\n').rstrip('\n').split('\n')
for i in range(len(lines)):
  if lines[i].startswith('Person 1: '):
    key = 'my_user'
    message = lines[i].replace('Person 1: ', '')
  elif lines[i].startswith('Person 2: '):
    key = 'other_user'
    message = lines[i].replace('Person 2: ', '')
  else:
    print(lines[i])
    raise 'invalid line'
```
The code below sets the time to -3 hours but this part is not mandatory, set it as per your timezone.
```
  created_at = (now + timedelta(hours=-3) + timedelta(minutes=i)).isoformat()
  create_message(
    client=ddb,
    message_group_uuid=message_group_uuid,
    created_at=created_at,
    message=message,
    my_user_uuid=users[key]['uuid'],
    my_user_display_name=users[key]['display_name'],
    my_user_handle=users[key]['handle']
  )
  ```
Create a new folder: `backend-flask/bin/ddb/patterns`. <br/>
**get-conversation**
```
#! /usr/bin/env python3

import boto3
import sys
import json
import datetime

attrs = {
  'endpoint_url': 'http://localhost:8000'
}

if len(sys.argv) == 2:
  if "prod" in sys.argv[1]:
    attrs = {}

dynamodb = boto3.client('dynamodb',**attrs)
table_name = 'cruddur-messages'

message_group_uuid = "5ae290ed-55d1-47a0-bc6d-fe2bc2700399"

# define the query parameters
year = str(datetime.datetime.now().year)
query_params = {
  'TableName': table_name,
  'ScanIndexForward': False, #default scans first to last but we want last to first
  'Limit': 20,
  'ReturnConsumedCapacity': 'TOTAL', #enables us to keep track of the dynamodb read/write units
  'KeyConditionExpression': 'pk = :pk AND begins_with(sk,:year)',
#   'KeyConditionExpression': 'pk = :pk AND sk BETWEEN :start_date AND :end_date',
  'ExpressionAttributeValues': {
    ':year': {'S': year },
    # ":start_date": { "S": "2023-03-01T00:00:00.000000+00:00" },
    # ":end_date": { "S": "2023-03-19T23:59:59.999999+00:00" },
    ':pk': {'S': f"MSG#{message_group_uuid}"},  #MSG = message_group_uuid
  },
}

# query the table
response = dynamodb.query(**query_params)

# print the items returned by the query
print(json.dumps(response, sort_keys=True, indent=2)) #json dumps make the print response prettier

# print the consumed capacity
print(json.dumps(response['ConsumedCapacity'], sort_keys=True, indent=2))

items = response['Items']
items.reverse() #reverse the order of the array of messages in order for last msg to be first

for item in items: #Printint the items in an easy to read way
  sender_handle = item['user_handle']['S']
  message       = item['message']['S']
  timestamp     = item['sk']['S']
  dt_object = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')
  formatted_datetime = dt_object.strftime('%Y-%m-%d %I:%M %p')
  print(f'{sender_handle: <12}{formatted_datetime: <22}{message[:40]}...')
```
**list-conversations**
```
#! /usr/bin/env python3

import boto3
import sys
import json
import os
import datetime

current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, '..', '..', '..'))
sys.path.append(parent_path)
from lib.db import db

attrs = {
  'endpoint_url': 'http://localhost:8000'
}

if len(sys.argv) == 2:
  if "prod" in sys.argv[1]:
    attrs = {}

dynamodb = boto3.client('dynamodb',**attrs)
table_name = 'cruddur-messages'
def get_my_user_uuid():
  sql = """
    SELECT 
      users.uuid
    FROM users
    WHERE
      users.handle =%(handle)s
  """
  uuid = db.query_value(sql,{
    'handle':  'andrewbrown'
  })
  return uuid

my_user_uuid = get_my_user_uuid()
print(f"my-uuid: {my_user_uuid}")

year = str(datetime.datetime.now().year)
# define the query parameters
query_params = {
  'TableName': table_name,
  'KeyConditionExpression': 'pk = :pk AND begins_with(sk,:year)',
  'ScanIndexForward': False,
  'ExpressionAttributeValues': {
    ':year': {'S': year },
    ':pk': {'S': f"GRP#{my_user_uuid}"}
  },
  'ReturnConsumedCapacity': 'TOTAL'
}

# query the table
response = dynamodb.query(**query_params)

# print the items returned by the query
print(json.dumps(response, sort_keys=True, indent=2))
```
**NB** 
In `list-conversations` the handle can also be `stevecmd`:
```
  uuid = db.query_value(sql,{
    'handle':  'stevecmd'
  })
```
We are using python version: 3.8, any other version would require one to change the date format here: `timestamp, '%Y-%m-%dT%H:%M:%S.%f%z'`
<br/>

To manually get the UUID, in `backend-flask` one can run:
```
./bin/db/connect
```
Once connected to the DB run:
```
SELECT uuid, handle FROM users
```
Add the function below into `backend-flask` > `lib` > `db.py`:
```
  def query_value(self,sql,params={}):
    self.print_sql('value',sql,params)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql,params)
        json = cur.fetchone() # Runs execute and fetch only one item from the DB
        return json[0]
```
The full `db.py` file will now be:
```
from psycopg_pool import ConnectionPool
import os
import re
import sys
from flask import current_app as app

class Db: #using a constructor to create an instance of the class
  def __init__(self):
    self.init_pool()

  def template(self,*args):
    pathing = list((app.root_path,'db','sql',) + args)
    pathing[-1] = pathing[-1] + ".sql"

    template_path = os.path.join(*pathing)

    green = '\033[92m'
    no_color = '\033[0m'
    print("\n")
    print(f'{green} Load SQL Template: {template_path} {no_color}')

    with open(template_path, 'r') as f:
      template_content = f.read()
    return template_content

  def init_pool(self):
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)
  # we want to commit data such as an insert
  # be sure to check for RETURNING in all uppercases
  def print_params(self,params):
    blue = '\033[94m'
    no_color = '\033[0m'
    print(f'{blue} SQL Params:{no_color}')
    for key, value in params.items():
      print(key, ":", value)

  def print_sql(self,title,sql,params={}):
    cyan = '\033[96m'
    no_color = '\033[0m'
    print(f'{cyan} SQL STATEMENT-[{title}]------{no_color}')
    print(sql,params) # Get richer data when we print out the values
  def query_commit(self,sql,params={}):
    self.print_sql('commit with returning',sql,params)

    pattern = r"\bRETURNING\b"
    is_returning_id = re.search(pattern, sql)

    try:
      with self.pool.connection() as conn:
        cur =  conn.cursor()
        cur.execute(sql,params)
        if is_returning_id:
          returning_id = cur.fetchone()[0]
        conn.commit() 
        if is_returning_id:
          return returning_id
    except Exception as err:
      self.print_sql_err(err)
  # when we want to return a json object
  def query_array_json(self,sql,params={}):
    self.print_sql('array',sql,params)

    wrapped_sql = self.query_wrap_array(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:  
        cur.execute(wrapped_sql,params)
        json = cur.fetchone()
        return json[0]
  # When we want to return an array of json objects
  def query_object_json(self,sql,params={}):

    self.print_sql('json',sql,params)
    self.print_params(params)
    wrapped_sql = self.query_wrap_object(sql)

    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql,params)
        json = cur.fetchone()
        if json == None:
          "{}"
          return "{}"
        else:
          return json[0]
  def query_value(self,sql,params={}):
    self.print_sql('value',sql,params)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql,params)
        json = cur.fetchone() # Runs execute and fetch only one item from the DB
        return json[0]
  def query_wrap_object(self,template):
    sql = f"""
    (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
    {template}
    ) object_row);
    """
    return sql
  def query_wrap_array(self,template):
    sql = f"""
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
    {template}
    ) array_row);
    """
    return sql
  def print_sql_err(self,err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    # get the line number when exception occured
    line_num = traceback.tb_lineno

    # print the connect() error
    print ("\npsycopg ERROR:", err, "on line number:", line_num)
    print ("psycopg traceback:", traceback, "-- type:", err_type)

    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")

db = Db()
```
Make the files executable:
```
chmod u+x bin/ddb/patterns/get-conversation
chmod u+x bin/ddb/patterns/list-conversations
```
Run the files:
```
./bin/ddb/patterns/get-conversation
./bin/ddb/patterns/list-conversations
```

# Cognito
Create the following file:
`bin` > `cognito` > `list-users`:
```
#!/usr/bin/env python3

import boto3
import os
import json

userpool_id = os.getenv("AWS_COGNITO_USER_POOL_ID") #using the env var user pool ID
client = boto3.client('cognito-idp')
params = {
  'UserPoolId': userpool_id,
  'AttributesToGet': [
      'preferred_username',
      'sub'
  ]
}
response = client.list_users(params)
users = response['Users'] #response from cognito

print(json.dumps(users, sort_keys=True, indent=2, default=str))

dict_users = {} #restructuring the data received into a dictionary  
for user in users:
  attrs = user['Attributes']
  sub    = next((a for a in attrs if a["Name"] == 'sub'), None) #sub is the key
  handle = next((a for a in attrs if a["Name"] == 'preferred_username'), None) #handle is the value
  dict_users[handle['Value']] = sub['Value']

print(json.dumps(dict_users, sort_keys=True, indent=2, default=str))
```
List users enables us to see the registered users on Cognito and we can then use that info elsewehere. <br/>
Run:
```
chmod u+x bin/cognito/list-users
```
Set your Cognito User Pool ID as a gitpod env var:
```
export env AWS_COGNITO_USER_POOL_ID="<insert user pool id>"
gp env AWS_COGNITO_USER_POOL_ID="<insert user pool id>"

```
On the CLI you can test your connection to Cognito by running:
```sh
aws cognito-idp list-users --user-pool-id=<insert user pool id>
```

Set the env var in our `docker-compose.yml` file: 
`REACT_APP_AWS_USER_POOLS_ID: "${AWS_COGNITO_USER_POOL_ID}"`

Modify the function: `def data_message_groups():` in `backend-flask/app.py` as:
```
@app.route("/api/message_groups", methods=['GET'])
def data_message_groups():
  access_token = extract_access_token(request.headers)
  try:
    claims = cognito_jwt_token.verify(access_token)
    # authenicatied request
    app.logger.debug("authenicated")
    app.logger.debug(claims)
    cognito_user_id = claims['sub']
    model = MessageGroups.run(cognito_user_id=cognito_user_id)
    if model['errors'] is not None:
      return model['errors'], 422
    else:
      return model['data'], 200
  except TokenVerifyError as e:
    # unauthenicatied request
    app.logger.debug(e)
    return {}, 401
```

Delete the following function:
```
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
```
Modify `message_groups.py` to incorporate Cognito:
```
from datetime import datetime, timedelta, timezone

from lib.ddb import Ddb
from lib.db import db

class MessageGroups:
  def run(cognito_user_id):
    model = {
      'errors': None,
      'data': None
    }

    sql = db.template('users','uuid_from_cognito_user_id')
    my_user_uuid = db.query_value(sql,{
      'cognito_user_id': cognito_user_id
    })

    print(f"UUID: {my_user_uuid}")

    ddb = Ddb.client()
    data = Ddb.list_message_groups(ddb, my_user_uuid)
    print("list_message_groups:",data)

    model['data'] = data
    return model
```
Create the following files in `backend-flask/db/sql
/users/` and save the attached code:
create_message_users.sql
```
SELECT 
  users.uuid,
  users.display_name,
  users.handle,
  CASE users.cognito_user_id = %(cognito_user_id)s
  WHEN TRUE THEN
    'sender'
  WHEN FALSE THEN
    'recv'
  ELSE
    'other'
  END as kind
FROM public.users
WHERE
  users.cognito_user_id = %(cognito_user_id)s
  OR 
  users.handle = %(user_receiver_handle)s
```
short.sql
```
SELECT
  users.uuid,
  users.handle,
  users.display_name
FROM public.users
WHERE 
  users.handle = %(handle)s
```
uuid_from_cognito_user_id.sql
```
SELECT
  users.uuid
FROM public.users
WHERE 
  users.cognito_user_id = %(cognito_user_id)s
LIMIT 1
```
Modify `HomeFeedPage.js`, `MessageGroupsPage.js`, `MessageGroupPage.js`, `MessageForm.js` and insert Cognito into them:
From:
```py
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`
        },
```
To:
```py
    headers: {
      'Authorization': `Bearer ${localStorage.getItem("access_token")}`,
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
```
Create the file: `frontend-react-js/src/lib/CheckAuth.js`:
```
import { Auth } from 'aws-amplify';

const checkAuth = async (setUser) => {
  Auth.currentAuthenticatedUser({
    // Optional, By default is false. 
    // If set to true, this call will send a 
    // request to Cognito to get the latest user data
    bypassCache: false 
  })
  .then((user) => {
    console.log('user',user);
    return Auth.currentAuthenticatedUser()
  }).then((cognito_user) => {
      setUser({
        display_name: cognito_user.attributes.name,
        handle: cognito_user.attributes.preferred_username
      })
  })
  .catch((err) => console.log(err));
};

export default checkAuth;
```

Modify `HomeFeedPage.js` and import our new `Checkauth` function and remove the original authentication:
Remove:
```
  const checkAuth = async () => {
    Auth.currentAuthenticatedUser({
      // Optional, By default is false. 
      // If set to true, this call will send a 
      // request to Cognito to get the latest user data
      bypassCache: false 
    })
    .then((user) => {
      console.log('user',user);
      return Auth.currentAuthenticatedUser()
    }).then((cognito_user) => {
        setUser({
          display_name: cognito_user.attributes.name,
          handle: cognito_user.attributes.preferred_username
        })
    })
    .catch((err) => console.log(err));
  };
```
Add:
```
import checkAuth from '../lib/CheckAuth';
```
```
checkAuth(setUser);
```
Remove the following function from MessageGroupsPage.js, MessageGroupPage.js :
```
  const checkAuth = async () => {
    console.log('checkAuth')
    // [TODO] Authenication
    if (Cookies.get('user.logged_in')) {
      setUser({
        display_name: Cookies.get('user.name'),
        handle: Cookies.get('user.username')
      })
    }
  };
```
and import CheckAuth:
```
import checkAuth from '../lib/CheckAuth';
checkAuth(setUser);
```
Set the endpoint URL in `docker-compose.yml`:
```py  
    backend-flask:
    environment:
      AWS_ENDPOINT_URL: "http://dynamodb-local:8000"
```
In `frontend-react-js` > `App.js` modify the code below:
```
  {
    path: "/messages/@:handle",
    element: <MessageGroupPage />
  },
```
to:
```  {
    path: "/messages/:message_group_uuid",
    element: <MessageGroupPage />
  },

```


Seed data from DynamoDB to see data:
`./bin/ddb/schema-load`
`./bin/ddb/seed`

Modify MessageGroupPage.js:
```
  const loadMessageGroupData = async () => {
    try {
      const handle = `@${params.handle}`;
      const backend_url = `${process.env.REACT_APP_BACKEND_URL}/api/messages/${handle}`
      const res = await fetch(backend_url, {
        method: "GET"
      });
```
to:
```py
  const loadMessageGroupsData = async () => {
    try {
      const backend_url = `${process.env.REACT_APP_BACKEND_URL}/api/message_groups`
      const res = await fetch(backend_url, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`
        },
        method: "GET"
      });

```
Modify MessageGroupItem.js:
From:
    `<Link className={classes()} to={`/messages/@`+props.message_group.handle}>` <br/> 
    to:
    `<Link className={classes()} to={`/messages/`+props.message_group.uuid}>`

From:
```
    if (params.handle == props.message_group.handle){
      classes.push('active')
    }
```
To:
```
  const classes = () => {
    let classes = ["message_group_item"];
    if (params.message_group.uuid == props.message_group.uuid){
      classes.push('active')
    }
    return classes.join(' ');
  }
```
Add Messages implementation to `app.py`:
```py
@app.route("/api/messages/<string:message_group_uuid>", methods=['GET'])
def data_messages(message_group_uuid):
  access_token = extract_access_token(request.headers)
  try:
    claims = cognito_jwt_token.verify(access_token)
    # authenicatied request
    app.logger.debug("authenicated")
    app.logger.debug(claims)
    cognito_user_id = claims['sub']
    model = Messages.run(
        cognito_user_id=cognito_user_id,
        message_group_uuid=message_group_uuid
      )
    if model['errors'] is not None:
      return model['errors'], 422
    else:
      return model['data'], 200
  except TokenVerifyError as e:
    # unauthenicatied request
    app.logger.debug(e)
    return {}, 401

@app.route("/api/messages", methods=['POST','OPTIONS'])
@cross_origin()
def data_create_message():
  message_group_uuid   = request.json.get('message_group_uuid',None)
  user_receiver_handle = request.json.get('handle',None)
  message = request.json['message']
  access_token = extract_access_token(request.headers)
  try:
    claims = cognito_jwt_token.verify(access_token)
    # authenicatied request
    app.logger.debug("authenicated")
    app.logger.debug(claims)
    cognito_user_id = claims['sub']
    if message_group_uuid == None:
      # Create for the first time
      model = CreateMessage.run(
        mode="create",
        message=message,
        cognito_user_id=cognito_user_id,
        user_receiver_handle=user_receiver_handle
      )
    else:
      # Push onto existing Message Group
      model = CreateMessage.run(
        mode="update",
        message=message,
        message_group_uuid=message_group_uuid,
        cognito_user_id=cognito_user_id
      )
    if model['errors'] is not None:
      return model['errors'], 422
    else:
      return model['data'], 200
  except TokenVerifyError as e:
    # unauthenicatied request
    app.logger.debug(e)
    return {}, 401
```
Modify `messages.py` to contain:
```py
from datetime import datetime, timedelta, timezone
from lib.ddb import Ddb
from lib.db import db

class Messages:
  def run(message_group_uuid,cognito_user_id):
    model = {
      'errors': None,
      'data': None
    }

    sql = db.template('users','uuid_from_cognito_user_id')
    my_user_uuid = db.query_value(sql,{
      'cognito_user_id': cognito_user_id
    })

    print(f"UUID: {my_user_uuid}")

    ddb = Ddb.client()
    data = Ddb.list_messages(ddb, message_group_uuid)
    print("list_messages")
    print(data)

    model['data'] = data
    return model

```
Modify `aws-bootcamp-cruddur-2023/frontend-react-js/src/components
/MessageForm.js` as follows:

```py
import './MessageForm.css';
import React from "react";
import process from 'process';
import { json, useParams } from 'react-router-dom';

export default function ActivityForm(props) {
  const [count, setCount] = React.useState(0);
  const [message, setMessage] = React.useState('');
  const params = useParams();

  const classes = []
  classes.push('count')
  if (1024-count < 0){
    classes.push('err')
  }

  const onsubmit = async (event) => {
    event.preventDefault();
    try {
      const backend_url = `${process.env.REACT_APP_BACKEND_URL}/api/messages`
      console.log('onsubmit payload', message)
      let json = { 'message': message }
      if (params.handle) {
        json.handle = params.handle
      } else {
        json.message_group_uuid = params.message_group_uuid
      }

      const res = await fetch(backend_url, {
        method: "POST",
        headers: {
          'Authorization': `Bearer ${localStorage.getItem("access_token")}`,
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)
      });
      let data = await res.json();
      if (res.status === 200) {
        console.log('data:',data)
        if (data.message_group_uuid) {
          console.log('redirect to message group')
          window.location.href = `/messages/${data.message_group_uuid}`
        } else {
          props.setMessages(current => [...current,data]);
        }
      } else {
        console.log(res)
      }
    } catch (err) {
      console.log(err);
    }
  }

  const textarea_onchange = (event) => {
    setCount(event.target.value.length);
    setMessage(event.target.value);
  }

  return (
    <form 
      className='message_form'
      onSubmit={onsubmit}
    >
      <textarea
        type="text"
        placeholder="send a direct message..."
        value={message}
        onChange={textarea_onchange} 
      />
      <div className='submit'>
        <div className={classes.join(' ')}>{1024-count}</div>
        <button type='submit'>Message</button>
      </div>
    </form>
  );
}

```






Week 5 Dynamodb stream
./bin/ddb/drop cruddur-messages prod

./bin/ddb/schema-load prod

Got to the AWS console > VPC > endpoint
Name > ddb-cruddur1
Service > dynamodb
VPC > default VPC
Select Routetable
Policy > Full access
Create endpoint


Lambda
Create Function: cruddur-messaging-stream-2
Runtime: Python
Create a new role with basic Lambda permissions
Advanced settings > Enable VPC > Select Default VPC > Choose 2 subnets > Choose Default SG > Create Function
The lambda:
```py
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource(
 'dynamodb',
 region_name='ca-central-1',
 endpoint_url="http://dynamodb.ca-central-1.amazonaws.com"
)

def lambda_handler(event, context):
  pk = event['Records'][0]['dynamodb']['Keys']['pk']['S']
  sk = event['Records'][0]['dynamodb']['Keys']['sk']['S']
  if pk.startswith('MSG#'):
    group_uuid = pk.replace("MSG#","")
    message = event['Records'][0]['dynamodb']['NewImage']['message']['S']
    print("GRUP ===>",group_uuid,message)
    
    table_name = 'cruddur-messages'
    index_name = 'message-group-sk-index'
    table = dynamodb.Table(table_name)
    data = table.query(
      IndexName=index_name,
      KeyConditionExpression=Key('message_group_uuid').eq(group_uuid)
    )
    print("RESP ===>",data['Items'])
    
    # recreate the message group rows with new SK value
    for i in data['Items']:
      delete_item = table.delete_item(Key={'pk': i['pk'], 'sk': i['sk']})
      print("DELETE ===>",delete_item)
      
      response = table.put_item(
        Item={
          'pk': i['pk'],
          'sk': sk,
          'message_group_uuid':i['message_group_uuid'],
          'message':message,
          'user_display_name': i['user_display_name'],
          'user_handle': i['user_handle'],
          'user_uuid': i['user_uuid']
        }
      )
      print("CREATE ===>",response)

```
Grant the role DynamoDb access: Add permissions > Attach policy > AWSLambdaInvocation-DynamoDB -- It provides read access to DynamoDB streams > add an inline policy
Delete the DynamoDb table, redeploy now that we have GSI, on console Turn on DynamoDB streams > New Image
On DynamoDb console create Trigger: `cruddur-messaging-stream-2`
Batch size 1
Turn on trigger

Deploy the lambda

Create the file `aws` > `lambdas` > `cruddur-messaging-stream`:
```py
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource(
 'dynamodb',
 region_name='us-east-1',
 endpoint_url="http://dynamodb.us-east-1.amazonaws.com"
)

def lambda_handler(event, context):
  pk = event['Records'][0]['dynamodb']['Keys']['pk']['S']
  sk = event['Records'][0]['dynamodb']['Keys']['sk']['S']
  if pk.startswith('MSG#'):
    group_uuid = pk.replace("MSG#","")
    message = event['Records'][0]['dynamodb']['NewImage']['message']['S']
    print("GRUP ===>",group_uuid,message)
    
    table_name = 'cruddur-messages'
    index_name = 'message-group-sk-index'
    table = dynamodb.Table(table_name)
    data = table.query(
      IndexName=index_name,
      KeyConditionExpression=Key('message_group_uuid').eq(group_uuid)
    )
    print("RESP ===>",data['Items'])
    
    # recreate the message group rows with new SK value
    for i in data['Items']:
      delete_item = table.delete_item(Key={'pk': i['pk'], 'sk': i['sk']})
      print("DELETE ===>",delete_item)
      
      response = table.put_item(
        Item={
          'pk': i['pk'],
          'sk': sk,
          'message_group_uuid':i['message_group_uuid'],
          'message':message,
          'user_display_name': i['user_display_name'],
          'user_handle': i['user_handle'],
          'user_uuid': i['user_uuid']
        }
      )
      print("CREATE ===>",response)
```
Save the policy as `cruddur-messaging-stream-dynamodb`.

Policy > stream > view cloudwatch logs > Check cloudwatch for any events once you try log in to the website and create a new message, for instance using Londo:`https://3000-stevecmd-awsbootcampcru-c7fjn6b3pzb.ws-eu107.gitpod.io/messages/new/londo`

Create `cruddur-message-stream-policy.json` in `aws > json > policies`:
```
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "VisualEditor0",
			"Effect": "Allow",
			"Action": [
				"dynamodb:PutItem",
				"dynamodb:DeleteItem",
				"dynamodb:Query"
			],
			"Resource": [
				"arn:aws:dynamodb:us-east-1:652162945585:table/cruddur-messages/index/message-group-sk-index",
				"arn:aws:dynamodb:us-east-1:652162945585:table/cruddur-messages"
			]
		}
	]
}
```
## Debugging:
I was running into errors regarding `cognito_jwt_token`, the fix was to implement the code below in `app.py` just after `app = Flask(__name__)`:
```py
cognito_jwt_token = CognitoJwtToken(
  user_pool_id=os.getenv("AWS_COGNITO_USER_POOL_ID"), 
  user_pool_client_id=os.getenv("AWS_COGNITO_USER_POOL_CLIENT_ID"),
  region=os.getenv("AWS_DEFAULT_REGION")
)
```
I was having issues trying to seed data hence I modified `backend-flask/bin/ddb/seed` to contain exceptions in order to catch the error and print debugging info:
```py
#!/usr/bin/env python3

import boto3
import os
import sys
from datetime import datetime, timedelta, timezone, date
import uuid

current_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.abspath(os.path.join(current_path, '..', '..'))
sys.path.append(parent_path)

from lib.db import db

attrs = {
    'endpoint_url': 'http://localhost:8000'
}

# unset endpoint URL for use with the production database
if len(sys.argv) == 2:
    if "prod" in sys.argv[1]:
        attrs = {}

ddb = boto3.client('dynamodb', **attrs)


def get_user_uuids():
    sql = """
        SELECT 
          users.uuid,
          users.display_name,
          users.handle
        FROM users
        WHERE
          users.handle IN(
            %(my_handle)s,
            %(other_handle)s
          )
      """
    try:
        users = db.query_array_json(sql, {
            'my_handle': 'stevecmd',
            'other_handle': 'andrewbrown'
        })
        my_user = next((item for item in users if item["handle"] == 'stevecmd'), None)
        other_user = next((item for item in users if item["handle"] == 'andrewbrown'), None)
        results = {
            'my_user': my_user,
            'other_user': other_user
        }
        print('get_user_uuids')
        print(results)
        return results
    except Exception as e:
        print(f"Error fetching user UUIDs: {e}")
        return {'my_user': None, 'other_user': None}


def create_message_group(client, message_group_uuid, my_user_uuid, last_message_at=None, message=None,
                          other_user_uuid=None, other_user_display_name=None, other_user_handle=None):
    table_name = 'cruddur-messages'
    record = {
        'pk': {'S': f"GRP#{my_user_uuid}"},
        'sk': {'S': last_message_at},
        'message_group_uuid': {'S': message_group_uuid},
        'message': {'S': message},
        'user_uuid': {'S': other_user_uuid},
        'user_display_name': {'S': other_user_display_name},
        'user_handle': {'S': other_user_handle}
    }

    try:
        response = client.put_item(
            TableName=table_name,
            Item=record
        )
        print(response)
    except Exception as e:
        print(f"Error creating message group: {e}")


def create_message(client, message_group_uuid, created_at, message, my_user_uuid, my_user_display_name, my_user_handle):
    record = {
        'pk': {'S': f"MSG#{message_group_uuid}"},
        'sk': {'S': created_at},
        'message_uuid': {'S': str(uuid.uuid4())},
        'message': {'S': message},
        'user_uuid': {'S': my_user_uuid},
        'user_display_name': {'S': my_user_display_name},
        'user_handle': {'S': my_user_handle}
    }

    table_name = 'cruddur-messages'

    try:
        response = client.put_item(
            TableName=table_name,
            Item=record
        )
        print(response)
    except Exception as e:
        print(f"Error creating message: {e}")


message_group_uuid = "5ae290ed-55d1-47a0-bc6d-fe2bc2700399"
now = datetime.now(timezone.utc).astimezone()
users = get_user_uuids()

# Debug prints
print("Users obtained from the database:")
print(users)

if users['my_user'] is None or users['other_user'] is None:
    sys.exit("Error: Unable to retrieve user UUIDs.")

create_message_group(
    client=ddb,
    message_group_uuid=message_group_uuid,
    my_user_uuid=users['my_user']['uuid'],
    other_user_uuid=users['other_user']['uuid'],
    other_user_handle=users['other_user']['handle'],
    other_user_display_name=users['other_user']['display_name'],
    last_message_at=now.isoformat(),
    message="this is a filler message"
)

lines = conversation.lstrip('\n').rstrip('\n').split('\n')

for i in range(len(lines)):
    if lines[i].startswith('Person 1: '):
        key = 'my_user'
        message = lines[i].replace('Person 1: ', '')
    elif lines[i].startswith('Person 2: '):
        key = 'other_user'
        message = lines[i].replace('Person 2: ', '')
    else:
        print(lines[i])
        sys.exit('Invalid line')

    created_at = (now + timedelta(hours=-3) + timedelta(minutes=i)).isoformat()

    create_message(
        client=ddb,
        message_group_uuid=message_group_uuid,
        created_at=created_at,
        message=message,
        my_user_uuid=users[key]['uuid'],
        my_user_display_name=users[key]['display_name'],
        my_user_handle=users[key]['handle']
    )

```
The results: <br />
Starting up DynamoDB-local was the issue. I then changed the code in `docker-compose.yml` to:
```py
  # Dynamo Database configuration ---- Start -----------
  dynamodb-local:
    # https://stackoverflow.com/questions/67533058/persist-local-dynamodb-data-in-volumes-lack-permission-unable-to-open-databa
    # We needed to add user:root to get this working.
    user: root
    # command: "-jar DynamoDBLocal.jar -sharedDb -dbPath ./data"
    command: "-jar DynamoDBLocal.jar -sharedDb -dbPath /home/dynamodblocal/data"
    image: "amazon/dynamodb-local:latest"
    container_name: dynamodb-local
    ports:
      - "8000:8000"
    volumes:
      - "./docker/dynamodb:/home/dynamodblocal/data"
    working_dir: /home/dynamodblocal
    networks:
      - internal-network
  # Dynamo Database configuration ---- End -----------
```
#### Routes: <br />
**Endpointes to take note of:** <br />
Health-check: 
```html
https://4567-<GITPOD Address>.gitpod.io/api/health-check
```
Home:
```html
https://4567-<GITPOD Address>.gitpod.io/api/activities/home
```
Notifications:
```html
https://4567-<GITPOD Address>.gitpod.io/api/activities/notifications
```
Messages:
```html
https://4567-<GITPOD Address>.gitpod.io/api/activities/messages
```
Message group:
```html
https://4567-stevecmd-awsbootcampcru-xxgo7kctld4.ws-eu108.gitpod.io/api/activities/message_group
```

## Serverless Caching

### Install Momento CLI tool

In your gitpod.yml file add:

```yml
  - name: momento
    before: |
      brew tap momentohq/tap
      brew install momento-cli
```

### Login to Momento

There is no `login` you just have to generate an access token and not lose it. 
 
You cannot rotate out your access token on an existing cache.

If you lost your cache or your cache was comprised you just have to wait for the TTL to expire.

> It might be possible to rotate out the key by specifcing the same cache name and email.
 ```sh
 momento account signup aws --email aravindv******@gmail.com --region ap-south-1
 ```

### Create Cache

```sh
export MOMENTO_AUTH_TOKEN=""
export MOMENTO_TTL_SECONDS="600"
export MOMENTO_CACHE_NAME="cruddur"
gp env MOMENTO_AUTH_TOKEN=""
gp env MOMENTO_TTL_SECONDS="600"
gp env MOMENTO_CACHE_NAME="cruddur"
```

> you might need to do `momento configure` since it might not pick up the env var in the CLI.
Create the cache:

```sh
momento cache create --name cruddur
```

## Save the work on its own branch named "week-5"
```sh
cd aws-bootcamp-cruddur-2024
git checkout -b week-5
```
<hr/>

## Commit
Add the changes and create a commit named: "Distributed Tracing"
```sh
git add .
git commit -m "DynamoDB and Serverless Caching"
```
Push your changes to the branch
```sh
git push origin week-5
```
<hr/>

### Tag the commit
```sh
git tag -a week-5-tag -m "Setting up DynamoDB and Serverless Caching"
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
git merge week-5
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
git branch -d week-5  # Deletes the local branch
git push origin --delete week-5  # Deletes the remote branch
```

> This was by far the most challenging week! Glad I made it through but I am not without battle scars! :fire: :alien: :sweat_drops: