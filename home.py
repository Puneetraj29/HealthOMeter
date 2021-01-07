from flask import Flask, render_template, url_for, flash, redirect
from flask import request
import joblib
from BC import app as bc
from diabetes import app as db
from kidney import app as kd
from heart import app as ht
from about import app as ab
import numpy as np

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('diseasePrediction.html')

@app.route('/BreastCancer')
def Breast_Cancer():
    return bc.cancer()

@app.route('/Diabetes')
def Diabetes():
    return db.cancer()

@app.route('/Kidney')
def Kidney():
    return kd.cancer()

@app.route('/Heart')
def Heart():
    return ht.cancer()

@app.route('/about')
def about():
    return ab.cancer()

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1, size)
    if (size == 5):
        loaded_model = joblib.load('BC\Breastcancer_model.pkl')
        result = loaded_model.predict(to_predict)
    elif (size == 6):
        loaded_model = joblib.load('diabetes\diabetes_model.pkl')
        result = loaded_model.predict(to_predict)
    elif (size == 7):
        loaded_model = joblib.load('kidney\kidney_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        # cancer
        if (len(to_predict_list) == 5):
            result = ValuePredictor(to_predict_list, 5)
        elif (len(to_predict_list) == 6):
            result = ValuePredictor(to_predict_list, 6)
        elif (len(to_predict_list) == 7):
            result = ValuePredictor(to_predict_list, 7)
    if(int(result)==1):
        prediction = "There's a high chance of you getting the disease, Please consult the doctor immediately"
    else:
        prediction = "Congratulations! No need to panic, you do not have any severe symptoms"

    return (render_template("result.html", prediction_text=prediction))


if __name__ == "__main__":
    app.run(debug=True)