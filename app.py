import pickle

import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = pickle.load(open('final_model(2).pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    p_class = request.form.get("pclass")
    sex = request.form.get("gender")
    age = request.form.get("age")
    embarked = request.form.get("embarked")
    title = request.form.get("title")
    deck = request.form.get("deck")

    if sex == 'Male':
        sex = 1
    if sex == 'Female':
        sex = 0
    if embarked == 'Cherbourg':
        embarked = 0
    if embarked == 'Queenstown':
        embarked = 1
    if embarked == 'Southampton':
        embarked = 2

    if title == 'Mr.':
        title = 1
    elif title == 'Master':
        title = 2
    elif title == 'Mrs.':
        title = 3
    elif title == 'Miss':
        title = 4
    else:
        title = 5

    features = [int(p_class), int(sex), int(age), int(embarked), int(title), int(deck)]
    ff = [np.array(features)]
    pred = model.predict(ff)[0]
    out=round(pred*100,2)
    return render_template('survival.html', pred_text='Survival Chances: {}%'.format(out))

if __name__ == "__main__":
    app.run(debug=True)









