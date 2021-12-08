FROM python:3.6-stretch
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "flask", "run", "--host=0.0.0.0" ]
