from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)   # __name__ == '__main__'

model = joblib.load(open('models/text_classification_model.joblib', 'rb'))

@app.route('/predict')
def predict():
    data = ['Love in the Time of Money is a visually stunning film to watch']
    prediction = model.predict(data)
    output_text = "Text: "+ str(data)
    output = "Class: " + str(prediction)
    return jsonify(output_text, output)

@app.route('/')
def index():
    return '<h1>Welcome to the Text Classifier</h1>'

if __name__ == '__main__':
    app.run(port=5000, debug=True)