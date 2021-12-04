FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN apk add mariadb-dev && apk add python2 py2-pip gcc python2-dev musl-dev
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ] 
CMD ["app.py"]