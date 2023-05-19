import pandas as pd
from flask import Flask
from flask import request
from flask import jsonify

from modules.insurance_model import InsuranceModal

app = Flask(__name__)

@app.route("/")
def index():
    return "project 7"

@app.route("/predict", methods=["POST"])
def predict():
    # pass
    data = request.get_json()
    df = pd.DataFrame(data, index=[0])
    x = InsuranceModal().runModel(df, typed='single')

    return jsonify({
        "status": "Predict",
        "predict_result": x
    })
