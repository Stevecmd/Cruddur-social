FROM python:3.10-slim-buster

# Inside container
# Make a new folder inside the container
WORKDIR /backend-flask

# Outside container -> Inside container
# Requirements contains the python libraries to be installed
COPY requirements.txt requirements.txt

# Update package list and install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Inside container
# installing python libraries
RUN pip3 install -r requirements.txt

# Outside container -> Inside container
# first period /backend-flask (outside container)
# second period /backend-flask (inside container) 
COPY . .

# Ensure the create script is executable
RUN chmod +x ./bin/db/*

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
