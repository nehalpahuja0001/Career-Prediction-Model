from flask import Flask, request, jsonify
import pandas as pd
# Import whatever library you used (sklearn, tensorflow, etc.)

app = Flask(__name__)

@app.route('/')
def home():
    return "Career Prediction Model is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    # This is where your model logic from the Notebook goes
    data = request.get_json()
    # prediction = model.predict(data) 
    return jsonify({"prediction": "Coming soon!"})

if __name__ == "__main__":
    # Railway provides a port dynamically, this line is CRITICAL
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
