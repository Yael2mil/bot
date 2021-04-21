import requests


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "0f0975e0-a225-11eb-a0f3-f13959cd449c060a1d66-f020-4e67-af08-43f214aec047"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

 
# CHANGE THIS to something you want your machine learning model to classify
demo = classify("ave")

label = demo["class_name"]
confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
# print ("result: '%s' with %d%% confidence" % (label, confidence))

if label == 'PezP':
    print("a")
elif label == "AveP":
    print("b")
elif label == "MamiferoP":
    print("c")
elif label == "ReptilP":
    print("d")
else:
    print(text)





