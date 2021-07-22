FROM python:3.7

RUN apt-get update\
    && apt-get install -y git file sudo zip 

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip" -o "awscliv2.zip"\
    && unzip awscliv2.zip\
    && sudo ./aws/install

COPY ./requirements.txt /home/sdk/
WORKDIR /home/sdk/
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

COPY . /home/sdk/
WORKDIR /home/sdk/src/
