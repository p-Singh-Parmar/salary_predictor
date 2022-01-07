import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('score.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For Rendering results on HTML GUI
    '''
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    predictions=model.predict(final_features)

    output=round(predictions[0],2)

    return render_template('score.html', prediction_text='Employee salary should be ${}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)
