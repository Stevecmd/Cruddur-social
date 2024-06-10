# Week 1 — App Containerization
This was the second week of the Bootcamp. In the end, I was succesful but it was quite intense as I wasted several days trying to
figure out what was causing the 404 error as shown below. 
>>404 Error Page not found
![404 Not Found](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/404%20error%20after%20docker%20run.JPG)
---
**In the end, I was victorious! Here's how I did it.**

>>**NB**: I just had to get my front end to communicate with the back end. I used the below referenced article to
guide me.

>>Article on Debugging Connection Refused
https://pythonspeed.com/articles/docker-connection-refused/
---

**Todo Checklist:**
- [x] [Watch How to Ask for Technical Help](https://www.youtube.com/watch?v=tDPqmwKMP7Y&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=29)
- [x] [Watch Grading Homework Summaries](https://www.youtube.com/watch?v=FKAScachFgk&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=25)
- [x] [Watch Week 1 - Live Streamed Video](https://www.youtube.com/watch?v=zJnNe5Nv4tE&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=22)
- [x] [Remember to Commit Your Code](https://www.youtube.com/watch?v=b-idMgFFcpg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=23)
- [x] [Watcked Chirag's Week 1 - Spending Considerations](https://www.youtube.com/watch?v=OAMHu1NiYoI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=24)
- [x] [Watched Ashish's Week 1 - Container Security Considerations](https://www.youtube.com/watch?v=OjZz4D0B-cA&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=25)
- [x] [Containerize Application (Dockerfiles, Docker Compose)](https://www.youtube.com/watch?v=zJnNe5Nv4tE&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=22)
- [x] [Document the Notification Endpoint for the OpenAI Document](https://www.youtube.com/watch?v=k-_o0cCpksk&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=27)
- [x] [Write a Flask Backend Endpoint for Notifications](https://www.youtube.com/watch?v=k-_o0cCpksk&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=27)
- [x] [Write a React Page for Notifications](https://www.youtube.com/watch?v=k-_o0cCpksk&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=27)
- [x] [Run DynamoDB Local Container and ensure it works](https://www.youtube.com/watch?v=CbQNMaa6zTg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=28)
- [x] [Run Postgres Container and ensure it works](https://www.youtube.com/watch?v=CbQNMaa6zTg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=28)
- [x] Complete 100% of the tasks

<hr/>

>>**Below is a step by step break down of my work. Use the Table of contents to jump to specific sections**

Table of contents
=================

<!--ts-->
   * [Todo Checklist](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#vscode-docker-extension)
   * [VSCode Docker Extension](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#vscode-docker-extension)
   * [Containerize Backend](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#containerize-backend)
      * [Run Python](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#run-python)
      * [Add Dockerfile](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#add-dockerfile)
      * [Build Container](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#build-container)
      * [Run Container](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#run-container)
        * [Attach Shell](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#attach-shell)
        * [Docker Run Container](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#docker-run-container)
        * [Docker Running container on Specific ports](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#docker-running-container-on-specific-ports)
      * [Get Container Images or Running Container Ids](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#get-container-images-or-running-container-ids)
      * [Getting the container image ID's via CLI - docker ps](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#getting-the-container-image-ids-via-cli---docker-ps)
      * [Getting the container image ID's via CLI - docker ps -a](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#getting-the-container-image-ids-via-cli---docker-ps--a) 
      * [Getting the docker images](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#getting-the-docker-images)     
   * [Containerize Frontend](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#containerize-frontend)
      * [Run NPM Install](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#run-npm-install)
      * [Create Docker File](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#create-docker-file)
      * [Multiple Containers](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#multiple-containers)
      * [Create a docker-compose file](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#create-a-docker-compose-file)
        * [Adding DynamoDB Local and Postgres](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#adding-dynamodb-local-and-postgres)
        * [DynamoDB Local](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#dynamodb-local)
        * [PostGres Install and configuration](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#postgres-install-and-configuration)
      * [Working App - Backend (Terminal)](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#working-app---backend-terminal)
      * [Working App - Backend JSON output](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#working-app---backend)
      * [Working App - Port 3000](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#working-app---port-3000) 
      * [Final image showing correct ports are running](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/week1.md#final-image-showing-correct-ports-are-running)     
<!--te-->

## VSCode Docker Extension

I used Docker for VSCode which makes it easy to work with Docker
**NB**I was using the VSCode application running on **GitPod**

https://code.visualstudio.com/docs/containers/overview

> Gitpod is preinstalled with this extension
<hr/>

## Containerize Backend

### Run Python

```sh
cd backend-flask
export FRONTEND_URL="*"
export BACKEND_URL="*"
python3 -m flask run --host=0.0.0.0 --port=4567
cd ..
```

- make sure to unlock the port on the port tab
- open the link for 4567 in your browser
- append to the url to `/api/activities/home`
- you should get back json

![Containerize Backend](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/Working%20container%20from%20docker%20image.JPG)

<hr/>

### Add Dockerfile

Create a file here: `backend-flask/Dockerfile`

```dockerfile
FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
```

<hr/>

### Build Container

![Build container](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/build%20container.JPG)

```sh
docker build -t  backend-flask ./backend-flask
```
![Backend flask](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/docker%20ps.JPG)

<hr/>

### Run Container

Run 
```sh
docker run --rm -p 4567:4567 -it backend-flask
FRONTEND_URL="*" BACKEND_URL="*" docker run --rm -p 4567:4567 -it backend-flask
export FRONTEND_URL="*"
export BACKEND_URL="*"
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
docker run --rm -p 4567:4567 -it  -e FRONTEND_URL -e BACKEND_URL backend-flask
unset FRONTEND_URL="*"
unset BACKEND_URL="*"
```

![Run Container](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%201/docker%20ps-a.JPG)

<hr/>

![Docker build confirmation](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/docker%20ps-a.JPG)

<hr/>

Run in background
```sh
docker container run --rm -p 4567:4567 -d backend-flask
```
<hr/>

#### Attach Shell
![Attach shell](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/Attach%20shell.png)

<hr/>

#### Docker Run Container
![Docker Run container](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/container%20run%201.JPG)

<hr/>

#### Docker Running container on Specific ports
![Docker Running container on Specific ports](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/container%20run%202.JPG)

<hr/>

Return the container id into an Env Vat
```sh
CONTAINER_ID=$(docker run --rm -p 4567:4567 -d backend-flask)
```

> docker container run is idiomatic, docker run is legacy syntax but is commonly used.

### Get Container Images or Running Container Ids

```
docker ps
docker images
```
#### Getting the container image ID's via CLI - docker ps
![Getting the container image ID's via CLI - docker ps](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/docker%20ps.JPG)

<hr/>

#### Getting the container image ID's via CLI - docker ps -a
![Getting the container image ID's via CLI - docker ps -a](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/docker%20ps-a.JPG)

<hr/>

#### Getting the docker images
![Getting the docker images](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/docker%20images.JPG)

### Send Curl to Test Server

```sh
curl -X GET http://localhost:4567/api/activities/home -H "Accept: application/json" -H "Content-Type: application/json"
```

### Check Container Logs

```sh
docker logs CONTAINER_ID -f
docker logs backend-flask -f
docker logs $CONTAINER_ID -f
```

###  Debugging  adjacent containers with other containers

```sh
docker run --rm -it curlimages/curl "-X GET http://localhost:4567/api/activities/home -H \"Accept: application/json\" -H \"Content-Type: application/json\""
```

busybosy is often used for debugging since it installs a bunch of things

```sh
docker run --rm -it busybosy
```

<hr/>

### Gain Access to a Container

```sh
docker exec CONTAINER_ID -it /bin/bash
```

> You can just right click a container and see logs in VSCode with Docker extension

<hr/>

### Delete an Image

```sh
docker image rm backend-flask --force
```

> docker rmi backend-flask is the legacy syntax, you might see this is old docker tutorials and articles.

> There are some cases where you need to use the --force

<hr/>

### Overriding Ports

```sh
FLASK_ENV=production PORT=8080 docker run -p 4567:4567 -it backend-flask
```
#### Overriding ports
!(https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/Unsetting%20URL's.JPG)

> Look at Dockerfile to see how ${PORT} is interpolated

#### Unset Backend and Front End ports
![Unset Backend and Front End ports](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/Unset%20backend%20and%20frontend.JPG)

<hr/>

#### Unset Backend and Front End URL's
![Unset Backend and Front End URL's](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/Unsetting%20URL's.JPG)

<hr/>

#### Unset the necessary ports for the app to work
![Unset the necessary ports for the app to work](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/Unlocked%20ports.JPG)

<hr/>

## Containerize Frontend
---

### Run NPM Install

We have to run NPM Install before building the container since it needs to copy the contents of node_modules

```
cd frontend-react-js
npm i
```
![NPM Install](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/npm%20install%20in%20frontendreact.JPG)

<hr/>

`Npm i` on startup is tyring to repeat, decided to automate the process.
![NPM Install Automation](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/automating%20npm%20install%20on%20startup.JPG)

<hr/>

### Create Docker File

Create a file here: `frontend-react-js/Dockerfile`

```dockerfile
FROM node:16.18

ENV PORT=3000

COPY . /frontend-react-js
WORKDIR /frontend-react-js
RUN npm install
EXPOSE ${PORT}
CMD ["npm", "start"]
```

<hr/>

### Build Container

```sh
docker build -t frontend-react-js ./frontend-react-js
```

<hr/>

### Run Container

```sh
docker run -p 3000:3000 -d frontend-react-js
```

<hr/>

## Multiple Containers

### Create a docker-compose file

Create `docker-compose.yml` at the root of your project.

```yaml
version: "3.8"
services:
  backend-flask:
    environment:
      FRONTEND_URL: "https://3000-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
      BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./backend-flask
    ports:
      - "4567:4567"
    volumes:
      - ./backend-flask:/backend-flask
  frontend-react-js:
    environment:
      REACT_APP_BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./frontend-react-js
    ports:
      - "3000:3000"
    volumes:
      - ./frontend-react-js:/frontend-react-js

# the name flag is a hack to change the default prepend folder
# name when outputting the image names
networks: 
  internal-network:
    driver: bridge
    name: cruddur
```

![Docker Compose Images](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/docker%20images.JPG)

<hr/>

## Adding DynamoDB Local and Postgres

We are going to use Postgres and DynamoDB local in future labs
We can bring them in as containers and reference them externally

Lets integrate the following into our existing docker compose file:

### Postgres

```yaml
services:
  db:
    image: postgres:13-alpine
    restart: always
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    ports:
      - '5432:5432'
    volumes: 
      - db:/var/lib/postgresql/data
volumes:
  db:
    driver: local
```

![PostGres and DynamoDB install](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/Added%20DynamoDB%20and%20Postgres.JPG)

<hr/>

![Current running ports](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/Opening%20all%20the%20ports.JPG)

<hr/>

To install the postgres client into Gitpod

```sh
  - name: postgres
    init: |
      curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
      echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
      sudo apt update
      sudo apt install -y postgresql-client-13 libpq-dev
```

<hr/>

### DynamoDB Local

```yaml
services:
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
```

<hr/>

Example of using DynamoDB local
https://github.com/100DaysOfCloud/challenge-dynamodb-local

![Using DynamoDB local](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/TestingDynamoDB.JPG)

<hr/>

## Create a table

```sh
aws dynamodb create-table \
    --endpoint-url http://localhost:8000 \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema AttributeName=Artist,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --table-class STANDARD
```

<hr/>

![DynamoDB Create table](hhttps://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/DynamoDB%20success.JPG)

<hr/>

![DynamoDB Create Item](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/createitem.JPG)
```sh
aws dynamodb put-item \
    --endpoint-url http://localhost:8000 \
    --table-name Music \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Somewhat Famous"}}' \
    --return-consumed-capacity TOTAL  
```
<hr/>

![DynamoDB Create Item in action](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/createitemMain.JPG)

<hr/>

![Code for DynamoDB List Tables](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/listTables.JPG)

## List Tables

```sh
aws dynamodb list-tables --endpoint-url http://localhost:8000
```

## Get Records

```sh
aws dynamodb scan --table-name cruddur_cruds --query "Items" --endpoint-url http://localhost:8000
````
![DynamoDB List Tables in action](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%201/List%20Tables%20Main.JPG)



<hr/>

```sh
aws dynamodb scan --table-name cruddur_cruds --query "Items" --endpoint-url http://localhost:8000
````
![Get Records](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/getRecordsMain.JPG)

## References For DynamoDB local

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.CLI.html
<hr/>

## Volumes

directory volume mapping

```yaml
volumes: 
- "./docker/dynamodb:/home/dynamodblocal/data"
```

named volume mapping

```yaml
volumes: 
  - db:/var/lib/postgresql/data

volumes:
  db:
    driver: local

```
<hr/>

### PostGres Install and configuration
![PostGres DB configuration](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/postgresDB%20connection.JPG)

<hr/>

![PostGres DB Success](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/postgresdbsuccessful%20connection.JPG)

<hr/>

### PostGres Install and configuration round 2 using SQLTool
![PostGres DB configuration2](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/postgres%20local%20access%20using%20SQLTool.JPG)

<hr/>

### PostGres local access
![PostGres local access](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/postgres%20local%20access.JPG)

<hr/>

![PostGres DB Success](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/postgresdbsuccessful%20connection.JPG)

<hr/>

#### Working App - Backend (Terminal)
![Working App - Backend (Terminal)](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/Running%20app%20on%20terminal.JPG)

<hr/>

#### Open API integration
![Open API](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/open%20api.JPG)
![Open API confirmation](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/open%20api%202.JPG)

<hr/>

#### Working App - Backend
![Working App - Backend](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/open%20api%202.JPG)

<hr/>

#### Notifications Backend
![Working App - Port 3000](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/notifications%20backend.JPG)

<hr/>

#### Working App - Port 3000
![Working App - Port 3000](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/Working%20application%20on%20port%203000.JPG)

<hr/>

#### Final image showing correct ports are running
![Final image showing correct ports are running](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/final%20correct%20ports%20are%20running.JPG)

<hr/>

[My EC2 Docker setup instructions](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/dockersetup.md)
<hr/>

$${\color{red}The End}$$

