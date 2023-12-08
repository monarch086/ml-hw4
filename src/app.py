import datetime as dt
from flask import Flask, request
from prediction import predict
import json
import numpy as np

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.int64):
            return int(obj)
        return json.JSONEncoder.default(self, obj)

app = Flask(__name__)

@app.route("/")
def home_page():
    return "<p><h2>KMA ML HW4: Prediction Web Server.</h2></p>"


@app.route(
    "/api/prediction",
    methods=["POST"],
)
def prediction_endpoint():
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