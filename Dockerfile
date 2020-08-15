FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/static
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt