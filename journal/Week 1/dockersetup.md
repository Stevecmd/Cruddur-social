# Docker:
In order for my docker container and images to be accessible remotely from Gitpod,
I had to create a docker hub username and password and save theses credentials. I then
had to undertake the following steps to upload my containers onto dockerhub:
1. In Gitpod type `docker images` to check how many images have you provisioned.
2. To pull the image from the registry I had to run code in the format `docker pull <image-name>:<tag>`, specifically;  `docker pull aws-bootcamp-cruddur-2023-backend-flask:latest`
3. I then had to tag and push each of the containers I had separately:
- `docker tag stevecmd/aws-bootcamp-cruddur-2023_frontend_react-js:latest stevecmd/aws-bootcamp-cruddur-2023_frontend_react-js:latest`
   `docker push stevecmd/aws-bootcamp-cruddur-2023_frontend_react-js:latest`
- `docker tag stevecmd/aws-bootcamp-cruddur-2023_backend_flask:latest stevecmd/aws-bootcamp-cruddur-2023_backend_flask:latest`
   `docker push stevecmd/aws-bootcamp-cruddur-2023_backend_flask:latest`
- `docker tag aws-bootcamp-cruddur-2023-frontend-react-js:latest stevecmd/aws-bootcamp-cruddur-2023-frontend-react-js:latest`
    `docker push stevecmd/aws-bootcamp-cruddur-2023-frontend-react-js:latest`
- `docker tag aws-bootcamp-cruddur-2023-backend-flask:latest stevecmd/aws-bootcamp-cruddur-2023-backend-flask:latest`
    `docker push stevecmd/aws-bootcamp-cruddur-2023-backend-flask:latest`
- `docker tag backend-flask:latest stevecmd/backend-flask:latest`
    `docker push stevecmd/backend-flask:latest`
This made the images available on docker hub for use wherever I want eg on an ec2 instance.
4. I then had to login into docker using `docker login`

## EC2 instance:
1. After creating the EC2 instance; to install docker via the ec2 instance user data, run: 
      ```
        #! /bin/sh
        yum update -y
        amazon-linux-extras install docker
        service docker start
        usermod -a -G docker ec2-user
        chkconfig docker on```
  
  Alternatively **SSH** into it and run:
  ``` $ sudo yum update -y
   $ sudo amazon-linux-extras install docker
   $ sudo service docker start
   $ sudo usermod -a -G docker ec2-user ```

2. I pulled the docker images by running:
    > `docker pull stevecmd/aws-bootcamp-cruddur-2023_frontend_react-js:latest`
    > `docker pull stevecmd/aws-bootcamp-cruddur-2023_backend_flask:latest`

3. I started the docker container by running:
    > `docker run -d -p 80:80 stevecmd/aws-bootcamp-cruddur-2023_frontend_react-js:latest`
    > `docker run -d -p 5000:5000 stevecmd/aws-bootcamp-cruddur-2023_backend_flask:latest`

4. To verify that the containers were running I ran `docker ps`

NB: The default format is: 
   > Tagging: `docker tag <image-id> <docker-hub-username>/<image-name>:<tag>`
   > Pushing: `docker push <docker-hub-username>/<image-name>:<tag>`
   > Pulling: `docker pull <image-name>:<tag>`