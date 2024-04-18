from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS
from Verification import FaceVerification

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(FaceVerification, '/verification')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)