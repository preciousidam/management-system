FROM python:3
ENV PYTHONUNBUFFERED=1
ENV REDIS_LOCAL='redis'
WORKDIR /management
COPY requirements.txt /management/requirements.txt
RUN pip install -r requirements.txt
COPY . /management/
