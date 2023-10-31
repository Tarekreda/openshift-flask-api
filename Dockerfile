FROM python:3.6
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
