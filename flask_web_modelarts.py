from flask import Flask
from flask import render_template, request
import requests

app = Flask(__name__)
url = "https://01516f373f434921a874bf502a986a58.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/4999c262-514e-424c-bc54-974abf850c25"
headers = { "X-Apig-AppCode": "8c4278dce8fe48f2a2f74ce6957ba2e5c8952d2c5876489b8bc7a8e132c8c020" }

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/recognize', methods=['POST'])
def call_modelArts():
    f = request.files['imgFilename']
    print('recognize: '+f.filename)
    files = {"images": (f.filename, f.read(), f.content_type)}
    resp = requests.post(url, headers=headers, files=files)  
    print('Result: '+ resp.text)
    jsonResult = resp.json()
    result = jsonResult['predicted_label']
    arScores = jsonResult['scores']
    predicted_score = 0
    for score in arScores:
        if score[0]== result:
            predicted_score = float(score[1])
        print("Results: %s : predicted: %2f" % (result,predicted_score))
    if resp.status_code == 200:
        strStatus = "I know this flower :)"
    else:
        strStatus= "Failed"
    return render_template("result.html", flower=result, status=strStatus, confidence = predicted_score)

if __name__ == "__main__":
 app.run('0.0.0.0', port=8000, debug=True)