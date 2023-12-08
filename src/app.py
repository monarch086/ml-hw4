# pylint: disable=import-error
'''Web-server for making predictions'''

import datetime as dt
import json
from flask import Flask, request
import numpy as np
from prediction import predict

class NumpyEncoder(json.JSONEncoder):
    '''Encoder to JSON'''
    def default(self, o):
        if isinstance(o, np.int64):
            return int(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)

@app.route("/")
def home_page():
    '''Home Page Endpoint'''
    return "<p><h2>KMA ML HW4: Prediction Web Server.</h2></p>"


@app.route(
    "/api/prediction",
    methods=["POST"],
)
def prediction_endpoint():
    '''Prediction Endpoint'''
    json_data = request.get_json()
    input_text = json_data.get("text")

    prediction = predict(input_text)

    time = dt.datetime.now()

    result = {
        "timestamp": time.isoformat(),
        "prediction": prediction,
    }

    json_str = json.dumps(result, cls=NumpyEncoder)

    return json_str

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
