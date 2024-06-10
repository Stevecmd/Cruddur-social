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

> This was by far the most challenging week! Glad I made it through but I am not without battle scars! :fire: :alien: :sweat_drops: