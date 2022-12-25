from flask import Flask
from flask import render_template, request
import requests


app = Flask(__name__)
url = "https://01516f373f434921a874bf502a986a58.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/4999c262-514e-424c-bc54-974abf850c25"
headers = { "X-Apig-AppCode": "8c4278dce8fe48f2a2f74ce6957ba2e5c8952d2c5876489b8bc7a8e132c8c020" }
dataFiles ={"images": ("14_1671157455635.jpeg", open("14_1671157455635.jpeg", "rb"), "image/jpeg", {})}

@app.route('/', methods=['GET'])
def index():
    return "Hello word from flaskkk"

@app.route('/test', methods=['GET'])
def call_modelArts_API():
    print("/test process")
    response = requests.post(url, headers=headers, files=dataFiles)
    jsonResults = response.json()
    result = jsonResults['predicted_label']
    arScores = jsonResults['scores']
    predicted_score = 0
    for score in arScores:
        if score[0]==result:
            predicted_score=float(score[1])
    resp = {}
    resp['result']= result
    resp['score']=predicted_score
    return resp

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000, debug=True)  