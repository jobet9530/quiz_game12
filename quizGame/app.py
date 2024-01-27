from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/api/data", methods=['GET'])
def get_data():
    
if __name__ == "__main__":
    app.run(debug=True)

