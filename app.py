import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

#load the model
model=pickle.load(open('regmodel.pkl','rb'))
scaler=pickle.load(open('scaler.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

'''
## test in postman 

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
    output=model.predict(new_data)
    print(output[0])
    return jsonify(output[0])
'''

@app.route('/predict',methods=['POST'])
def predict():
    data= [float(x) for x in request.form.values()]
    final_input= np.array(data).reshape(1,-1)
    scaled_input= scaler.transform(final_input)
    prediction=model.predict(scaled_input)[0]
    price=prediction*1000
    return render_template("home.html",prediction_text=f"Estimated house price is ${price:,.2f}")

if __name__=="__main__":
    app.run(debug=True)





