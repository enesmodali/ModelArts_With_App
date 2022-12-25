import requests

url = "https://01516f373f434921a874bf502a986a58.apig.ap-southeast-3.huaweicloudapis.com/v1/infers/4999c262-514e-424c-bc54-974abf850c25"

headers = { "X-Apig-AppCode": "8c4278dce8fe48f2a2f74ce6957ba2e5c8952d2c5876489b8bc7a8e132c8c020" }

dataFiles ={"images": ("14.jpeg", open("14.jpeg", "rb"), "image/jpeg", {})}

try:
    response = requests.post(url, headers=headers, files=dataFiles)
    print(response.text)
    print(response.status_code)
    jsonResult = response.json()
    result = jsonResult['predicted_label']
    arScores = jsonResult['scores']
    predicted_score = 0
    for score in arScores:
        # print(score)
        if score[0]==result:
            predicted_score = float(score[1])
    print("Result: %s : predicted: %.2f" % (result,predicted_score))
except IOError as e:
    print("Error: ", str(e))    
