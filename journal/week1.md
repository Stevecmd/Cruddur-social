# Week 1 — App Containerization
This was the second week of the Bootcamp. In the end, I was succesful but it was quite intense as I wasted several days trying to
figure out what was causing the 404 error as shown below. 
>>404 Error Page not found
![404 Not Found](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/404%20error%20after%20docker%20run.JPG)
---
**In the end, I was victorious! Here's how I did it.**

>>**NB**: I just had to get my front end to communicate with the back end. I used the referenced article below to
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

Container repo's:
- [DockerHub](https://hub.docker.com/)
- [Jfrog](https://jfrog.com/) - For artifacts / images

## Containerize Backend

![Containerize Backend](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/Working%20container%20from%20docker%20image.JPG)

<hr/>

### Containerize Backend
> Create Docker File
Create a file here: `backend-flask/Dockerfile`

```dockerfile
FROM python:3.10-slim-buster

# Inside container
# Make a new folder inside the container
WORKDIR /backend-flask

# Outside container -> Inside container
# Requirements contains the python libraries to be installed
COPY requirements.txt requirements.txt

# Inside container
# installing python libraries
RUN pip3 install -r requirements.txt

# Outside container -> Inside container
# first period /backend-flask (outside container)
# second period /backend-flask (inside container) 
COPY . .

# Setting env vars inside container
# and will remain set while container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}
# The command itself is invoking the Python interpreter (python3) with
# the -m flag, which allows running a module as a script.
# The module being run is flask, and the additional arguments provided
# to Flask are run --host=0.0.0.0 --port=4567.
# This essentially starts a Flask web application and
# binds it to all network interfaces (0.0.0.0) on port 4567.

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
```

<hr/>

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

<bold>NB:</bold>To unset the env vars run the code below:
```sh
unset FRONTEND_URL
unset BACKEND_URL
```
Confirm that they are unset:
```sh
env | grep FRONTEND_URL
env | grep BACKEND_URL
```
cd into the project directory 'aws-bootcamp-cruddur-2024':
```sh
  cd aws-bootcamp-cruddur-2024
```

### Build Container

![Build container](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/build%20container.JPG)

```sh
docker build -t  backend-flask ./backend-flask
```
![Backend flask](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/docker%20ps.JPG)

<hr/>

### Run Container

* Make sure that the image builds succesfully then run it:
```sh
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask
```
If the command runs successfully, exit the server by pressing 'Ctrl+C':
On the terminal set the env vars:
```sh
set FRONTEND_URL="*"
set BACKEND_URL="*"
```
Run the container
```sh
docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' -d backend-flask
```
The command above upon running succesfully will output your container number.

Visit the port link in a new Tab and make sure to append '/api/activities/home' to the URL, you should get Javascript response.


![Run Container](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%201/docker%20ps-a.JPG)

<hr/>

On gitpod open a new terminal and run the code below to see the running docker containers:
```sh
  docker ps
```
To see the images available run:
```sh
  docker images
```

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

Return the container id into an Env Var
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
docker image rm backend-flask
```

> docker rmi backend-flask is the legacy syntax, you might see this is old docker tutorials and articles.

> There are some cases where you need to use the --force

**NB** to delete an image we use the 'rm' flag to make sure the container does not simply stop and stay in a suspended
state, 'rm' deletes the container.

```sh
docker image rm backend-flask --force
```

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

```sh
cd frontend-react-js
npm i
```
![NPM Install](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/npm%20install%20in%20frontendreact.JPG)

<hr/>

`Npm i` on startup is trying to repeat, decided to automate the process.
![NPM Install Automation](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/automating%20npm%20install%20on%20startup.JPG)

<hr/>

### Create Frontend Docker File

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

Create `docker-compose.yml` at the root' of your project ie within 'aws-bootcamp-cruddur-2024'. 
and put the following code in...

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
Once done run docker compose up on the file docker-compose.yml to validate the file and see whether it runs.
Unlock port 3000 and 4567 and ensure they are in a running state.
Port 3000 should link to the running Cruddur website.
If the website does not have some mockposts or any other error, check the website logs to ensure there are no errors such as 'CORS'

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

To install the postgres client into Gitpod, add the code below to the gitpod.yml file:

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
Add DynamoDB as a service to the docker-compose.yml file after postgres:
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

## Open-API

### Document the Notification Endpoint for the OpenAPI Document, Write a Flask Backend Endpoint for Notifications, and Write a React Page for Notifications
In this task, we created the openapi-3.0.yml file as a standard for defining APIs. The API is providing us with mock data, as there's currently no database hooked to the backend. 

[Open API](https://dash.readme.com/)

[Open API Initiative Registry](https://spec.openapis.org/)
> To understand the Open Api file in: 'backend-flask/openapi-3.0.yml'; 
  visit the link above.

We added a new section to the Open Api file at line 150 directly after:
```yml 
  $ref: '#/components/schemas/Message'
```
The section to add is as below:

```yml
  /api/activities/notifications:
    get:
      description: 'Return a feed of activity for all of those that I follow'
      tags:
        - activities
      parameters: []
      responses:
        '200':
          description: Returns an array of activities
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Activity'
```

To write a Flask Backend Endpoint for Notifications, we selected the 'app.py' file in 'backend-flask' and added the following to create a micro service:
At Line 7 add:

```Python

from services.notifications_activities import * 

```
Define a route for the notifications endpoint in the Flask app:
Line 68, after: 
```python
  @app.route("/api/activities/home"
```
...insert the code code below:

```Python
@app.route("/api/activities/notifications", methods=['GET'])
def data_notifications():
  data = NotificationsActivities.run()
  return data, 200
```
In 'backend-flask/services' we defined the micro service notifications_activites.py:

```Python
from datetime import datetime, timedelta, timezone
class NotificationsActivities:
  def run():
    now = datetime.now(timezone.utc).astimezone()
    results = [{
      'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      'handle':  'coco',
      'message': 'I am white unicorn',
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
    ]
    return results
```

For the Frontend, to implement the notifications tab, we went to the frontend-react-js folder>src. We accessed App.js, and added something new to import at line 4:

```Javascript
import NotificationsFeedPage from './pages/NotificationsFeedPage';
```

Line 23 - Using react-router, we added a new path for the element:

```Javascript
  {
    path: "/notifications",
    element: <NotificationsFeedPage />
  },
```

Then under 'frontend-react-js/src/pages', we created the pages NotificationsFeedPage.js and NotificationsFeedPage.css.
Add the code below to 'NotificationsFeedPage.js':

```Javascript
import './NotificationsFeedPage.css';
import React from "react";

import DesktopNavigation  from '../components/DesktopNavigation';
import DesktopSidebar     from '../components/DesktopSidebar';
import ActivityFeed from '../components/ActivityFeed';
import ActivityForm from '../components/ActivityForm';
import ReplyForm from '../components/ReplyForm';

// [TODO] Authenication
import Cookies from 'js-cookie'

export default function NotificationsFeedPage() {
  const [activities, setActivities] = React.useState([]);
  const [popped, setPopped] = React.useState(false);
  const [poppedReply, setPoppedReply] = React.useState(false);
  const [replyActivity, setReplyActivity] = React.useState({});
  const [user, setUser] = React.useState(null);
  const dataFetchedRef = React.useRef(false);

  const loadData = async () => {
    try {
      const backend_url = `${process.env.REACT_APP_BACKEND_URL}/api/activities/notifications`
      const res = await fetch(backend_url, {
        method: "GET"
      });
      let resJson = await res.json();
      if (res.status === 200) {
        setActivities(resJson)
      } else {
        console.log(res)
      }
    } catch (err) {
      console.log(err);
    }
  };

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

  React.useEffect(()=>{
    //prevents double call
    if (dataFetchedRef.current) return;
    dataFetchedRef.current = true;

    loadData();
    checkAuth();
  }, [])

  return (
    <article>
      <DesktopNavigation user={user} active={'notifications'} setPopped={setPopped} />
      <div className='content'>
        <ActivityForm  
          popped={popped}
          setPopped={setPopped} 
          setActivities={setActivities} 
        />
        <ReplyForm 
          activity={replyActivity} 
          popped={poppedReply} 
          setPopped={setPoppedReply} 
          setActivities={setActivities} 
          activities={activities} 
        />
        <ActivityFeed 
          title="Notifications" 
          setReplyActivity={setReplyActivity} 
          setPopped={setPoppedReply} 
          activities={activities} 
        />
      </div>
      <DesktopSidebar user={user} />
    </article>
  );
}
```


Then at the bottom of the docker-compose.yml file, we added the rest of the Postgress code for the volumes:

```yml
volumes:
  db:
    driver: local
```

To test your local DynamoDB orchestration run:
## Run Docker Local

```
docker-compose up
```
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

## Create an Item

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

## List Tables

![Code for DynamoDB List Tables](https://github.com/Stevecmd/Cruddur-social/blob/main/journal/Week%201/listTables.JPG)

```sh
aws dynamodb list-tables --endpoint-url http://localhost:8000
```

## Get Records

```sh
aws dynamodb scan --table-name cruddur_cruds --query "Items" --endpoint-url http://localhost:8000
````
![DynamoDB List Tables in action](https://github.com/Stevecmd/aws-bootcamp-cruddur-2023/blob/main/journal/Week%201/List%20Tables%20Main.JPG)

<hr/>

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

Named volume mapping

```yaml
volumes: 
  - db:/var/lib/postgresql/data

volumes:
  db:
    driver: local

```
<hr/>

### PostGres Install and configuration

To add Postgres as a dependency that installs on startup, add the code below in the '.gitpod.yml' file:
Place it under the vs-code extensions,
```yml
    - cweijan.vscode-mysql-client2
```
Make sure to install postgres via the terminal, run:
```sh
      curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc|sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
      echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
      sudo apt update
      sudo apt install -y postgresql-client-13 libpq-dev
```

To test the postgres installation run the code below:
```sh
psql -Upostgres --host localhost
Press Enter once asked for a password or input 'password'
```

## Extra

Implement a healthcheck in the Docker compose file --> 'docker-compose.yml' :
```yaml
    healthcheck:
      test: curl --fail http://localhost || exit 1
      interval: 60s
      retries: 5
      start_period: 20s
      timeout: 10s
```

- [PostGres useful tips - CLI](https://www.prisma.io/dataguide/postgresql/setting-up-a-local-postgresql-database#setting-up-postgresql-on-linux)

Hardcoded pass for cruddur users = 1234

## Save the work on its own branch named "week-1"
```sh
cd aws-bootcamp-cruddur-2024
git checkout -b week-1
```
<hr/>

## Commit
Add the changes and create a commit named: "App Containerization"
```sh
git add .
git commit -m "App Containerization"
```
Push your changes to the branch
```sh
git push origin week-1
```
<hr/>

### Tag the commit
```sh
git tag -a week-1 -m "Setting up App Containerization"
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
git merge week-1
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
git branch -d week-1  # Deletes the local branch
git push origin --delete week-1  # Deletes the remote branch
```

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
