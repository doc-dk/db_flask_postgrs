FROM python:latest
MAINTAINER Devaki Kelkar "dakelkar@gmail.com"
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install -i https://test.pypi.org/simple/ flask-bootstrap-4-alpha
RUN mkdir /app/logs
RUN touch /app/logs/service.log
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]