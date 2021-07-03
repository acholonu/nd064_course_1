import typing
from flask import Flask
from flask import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/metric")
def get_metrics():
    response = app.response_class(
        response = json.dumps('{"UserCount": 140, "UserCountActive": 23}'), # return data
        status=200, #everything is good
        mimetype='application/json'
    )
    return response

@app.route("/status")
def get_status():
    # API Return call for the web response
    response = app.response_class(
        response = json.dumps({"result": "OK - healthy"}), # return data
        status=200, #everything is good
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
