# Week 4 — Databases: Postgres - RDS and SQL
This was technically the fifth week of the Bootcamp. 

(The Hyperlinks in the table below link to the training videos)

**Todo Checklist:**
- [x] [Watched Ashish's Week 4 - Security Considerations](https://www.youtube.com/watch?v=UourWxz7iQg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=45 )
- [x] [Create RDS Postgres Instance](https://www.youtube.com/watch?v=EtD7Kv5YCUs&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=46 )
- [x] [Bash scripting for common database actions](https://www.youtube.com/watch?v=EtD7Kv5YCUs&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=46)
- [x] [Install Postgres Driver in Backend Application](https://www.youtube.com/watch?v=Sa2iB33sKFo&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=47)
- [x] [Connect Gitpod to RDS Instance](https://www.youtube.com/watch?v=Sa2iB33sKFo&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=47)
- [x] [Create Congito Trigger to insert user into database](https://www.youtube.com/watch?v=7qP4RcY2MwU&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=48)
- [x] [Create new activities with a database insert](https://www.youtube.com/watch?v=fTksxEQExL4&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=49 )
- [x] Complete 100% of the tasks

<hr/>

<hr/>

| Homework      | Completed     | Not Completed  |
| ------------- |:-------------:| -----:|
| [Week 4 - Relational databases](https://www.youtube.com/watch?v=EtD7Kv5YCUs)  | ✔     |    |
| [Week 4 - SQL RDS](https://www.youtube.com/watch?v=Sa2iB33sKFo)   | ✔ |  |
| [Week 4 - Cognito Post Confirmation Lambda](https://www.youtube.com/watch?v=7qP4RcY2MwU)  | ✔     |    |
| [Week 4 - Creating Activities](https://www.youtube.com/watch?v=fTksxEQExL4) | ✔      |   |
| [Ashish's Week 4 - Security Considerations](https://www.youtube.com/watch?v=UourWxz7iQg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=46)|✔      |   |

<hr/>

|    | Table of contents - Steps taken to complete Week 4 assignments                                                                                                                                                                         |
|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | [Console - Lambda initial setup 1](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#console---lambda-initial-setup-1)                                |
| 2  | [Console - Lambda initial setup 2](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#console---lambda-initial-setup-2)                                                |
| 3  | [Console - Lambda initial setup 3](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#console---lambda-initial-setup-3)                                               |
| 4  | [Console - Lambda creation success](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#console---lambda-creation-success)                                    |
| 5  | [RDS database creation commands](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#rds-database-creation-commands)                                                  |
| 6  | [Database creation success](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#database-creation-success)                           |
| 7  | [Temporarily stopping RDS](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#temporarily-stopping-rds)                                              |
| 8  | [Initial Postgres Connection](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#initial-postgres-connection)                                  |
| 9  | [Creating the Cruddur Database](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#creating-the-cruddur-database)                                                     |
| 10 | [Running SQL script to load the DB schema](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#running-sql-script-to-load-the-db-schema)                                  |
| 11 | [Exporting PSQL connection URL](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#exporting-psql-connection-url)                                                    |
| 12 | [Creation of Database Binary files](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#creation-of-database-binary-files)                                     |
| 13 | [Modifying Binary file permissions](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#modifying-binary-file-permissions)                                                        |
| 14 | [Dropping the database](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#dropping-the-database)                                                             |
| 15 | [Database creation script](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#database-creation-script)                                                             |
| 16 | [Setting the Database schema path](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#setting-the-database-schema-path)                          |
| 17 | [Loading the Database schema](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#loading-the-database-schema) |
| 18 | [Changing modes and running in production mode](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#changing-modes-and-running-in-production-mode)                                                         |
| 19 | [Implementing colored responses](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#implementing-colored-responses)                                                                   |
| 20 | [Successful table creation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#successful-table-creation)                                                           |
| 21 | [Exporting the PSQL database connection variable](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#setting-the-psql-database-connection-variable)                                             |
| 22 | [View created tables](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#view-created-tables)                                                           |
| 23 | [Database creation and loading the database schema](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#database-creation-and-loading-the-database-schema)                                                           |
| 24 | [Setting the production database variables](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#setting-the-production-database-variables)                                                           |
| 25 | [Setting Database credentials as enviromental variables](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#setting-database-credentials-as-enviromental-variables)                                                           |
| 26 | [Successful psql connection](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week4.md#successful-psql-connection)                                                           |                                                                                                                                       



## Console - Lambda initial setup 1
![Console - Lambda initial setup 1](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/Lambda%20setup%201.JPG)

## Console - Lambda initial setup 2  
![Console - Lambda initial setup 2](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/Lambda%20setup%202..JPG)

## Console - Lambda initial setup 3
![Console - Lambda initial setup 3](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/Lambda%20setup%203.JPG)

## Console - Lambda creation success
![Console - Lambda creation success](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/lamda%20creation%20success.JPG)

## RDS database creation commands
![RDS database creation commands](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/rds%20creation%20commands.JPG)

## Database creation success
![Database creation success](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/DB%20creation%20success.JPG)

## Temporarily stopping RDS
![Temporarily stopping RDS](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/Stopping%20RDS%20temporarily.JPG)

## Initial Postgres Connection
![Initial Postgres Connection](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/Initial%20connection%20to%20postgres.JPG)

## Creating the Cruddur Database
![Creating the Cruddur Database](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/create%20cruddur%20db.JPG)

## Running SQL script to load the DB schema
![Running SQL script to load the DB schema](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/running%20the%20sql%20script.JPG)

## Exporting PSQL connection URL
![Exporting PSQL connection URL](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/exporting%20psql%20connection%20url.JPG)

## Creation of Database Binary files
![Creation of Database Binary files](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/creating%20db%20binary%20files.JPG)

## Modifying Binary file permissions
![Modifying Binary file permissions](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/modifying%20bin%20file%20permissions.JPG)

## Dropping the database
![Dropping the database](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/drop%20database.JPG)

## Database creation script
![Database creation script](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/db%20create%20script.JPG)

## Setting the Database schema path
![Setting the Database schema path](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%203/confirming%20email%20via%20terminal.JPG)

## Loading the Database schema
![Loading the Database schema](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/schema%20path.JPG)

## Changing modes and running in production mode
![Changing modes and running in production mode](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/running%20in%20prod%20mode.JPG)

## Implementing colored responses
![Implementing colored responses](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/implementing%20color%20in%20response.JPG)

## Successful table creation
![Successful table creation](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/table%20creation%20success.JPG)

## Setting the PSQL database connection variable
![Setting the PSQL database connection variable](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/exporting%20psql%20connection%20url.JPG)

## View created tables
![View created tables](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/view%20tables.JPG)

## Database creation and loading the database schema
![Database creation and loading the database schema](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/create%20db%20and%20load%20schema.JPG)

## Setting the production database variables
![Setting the production database variables](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/setting%20the%20production%20db%20variables.JPG)

## Setting Database credentials as enviromental variables
![Setting Database credentials as enviromental variables](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/setting%20db%20creds%20as%20env.JPG)

## Successful psql connection
![Successful psql connection](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%204/successful%20psql%20connection.JPG)