from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route("/status")
def healthcheck():
    response=app.response_class(
        response = json.dumps({"result":"OK - I'm fine"}),
        status = 200,
        mimetype='application/json'
    )
    app.logger.info('Status request sucessfull')
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response = json.dumps({"status:":"sucess","code":0,"data":{"Usercount":140,"UsercountActive":23}}),
        status  = 200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request sucessfull')
    return response

@app.route("/")
def hello():
    app.logger.info('Main request sucessfull')
    return "Hello World! This is Mohammed"

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
