from flask import Flask, render_template, request
import joblib
import numpy as np

model = joblib.load("ridge_insurance_model.pkl")
le_smoker = joblib.load("smoker_encoder.pkl")
le_region = joblib.load("region_encoder.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            age = float(request.form["age"])
            bmi = float(request.form["bmi"])
            children = int(request.form["children"])
            smoker = le_smoker.transform([request.form["smoker"]])[0]
            region = le_region.transform([request.form["region"]])[0]
            values = [age, bmi, children, smoker, region]
            prediction = model.predict(np.array([values]))[0]
            prediction = round(prediction, 2)
        except:
            prediction = "Invalid input"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
