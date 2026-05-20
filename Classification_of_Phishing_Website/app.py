
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']

    # Dummy ML prediction logic
    result = random.choice(["Safe Website", "Phishing Website"])

    return render_template('index.html', prediction=result, url=url)

if __name__ == '__main__':
    app.run(debug=True)
