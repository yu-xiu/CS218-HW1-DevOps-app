# use pyton runtime as a parent image with slim variant, which has a smaller image size and faster build times
FROM python:3.9-slim

# set the working dir in the container
WORKDIR /app

# copy the app_server.py from local host machine to the /app directory in the contianer
COPY app_server.py .

# copy requirements to install all the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# specify the command to run the server/app when the container starts
CMD ["python", "app_server.py"]