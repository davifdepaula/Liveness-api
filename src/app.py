from liveness_demo import predict
from flask import Flask

app = Flask(__name__)

@app.route('/predict', methods = ['GET'])
def post():
    predict()


app.run()