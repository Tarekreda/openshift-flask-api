FROM python:3.6
ADD . /app
WORKDIR /app
EXPOSE 8080
RUN pip install -r requirements.txt
