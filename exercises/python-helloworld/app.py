import typing
import logging
from flask import Flask
from flask import json
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"

@app.route("/metric")
def get_metrics():
    timestamp = datetime.now()
    response = app.response_class(
        response = json.dumps({"UserCount": 140, "UserCountActive": 23}), # return data
        status=200, # status of the request - everything is good
        mimetype='application/json'
    )

    ## log line
    app.logger.info('Metrics request successfull')
    return response

@app.route("/status")
def get_status():
    # API Return call for the web response
    timestamp = datetime.now()
    response = app.response_class(
        response = json.dumps({"result": "OK - healthy"}), # return data
        status=200, #status of the request - everything is good
        mimetype='application/json'
    )

    ## log line
    app.logger.info('Status request successfull')
    return response

if __name__ == "__main__":
    ## stream logs to app.log file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
