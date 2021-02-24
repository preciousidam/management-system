FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /management
COPY requirements.txt /management/
RUN pip install -r requirements.txt
COPY . /management/