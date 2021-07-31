FROM python:3.8
LABEL maintainer="Mohammed Abuibaid"

COPY ./exercises/python-helloworld/. /app
WORKDIR /app
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "app.py" ]
# copied from solution
