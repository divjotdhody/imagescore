FROM ubuntu:18.04
EXPOSE 5000

RUN apt-get update -y
RUN apt-get install python3.6 -y
RUN apt-get install python3-pip -y

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt
COPY . /app


CMD [ "python3", "app.py" ]