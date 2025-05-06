# Flask API to serve the model
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return 'Model is running!'

if __name__ == '__main__':
    app.run(debug=True)