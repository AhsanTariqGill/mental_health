from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder='template')

model=pickle.load(open('Fraud.pkl','rb'))



@app.route('/')
def hello_world():
    print(app.template_folder)
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    print(int_features)
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    pred = model.predict(final)
    print(pred)
    NotFraudProb = prediction[0][0]
    print(NotFraudProb)
    FruadProb = prediction[0][1]
    print(FruadProb)

    if pred == 1:
        return render_template('index.html',pred='Fraudlant Transaction.\nWith probability of {}'.format(FruadProb))
    else:
        return render_template('index.html',pred='Not a fraudent transaction.\n With probability of {}'.format(NotFraudProb))


if __name__ == '__main__':
    app.run(debug=True)
