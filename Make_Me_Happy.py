import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "526fecd0-aa3b-11e9-8956-a9aa867fc997382b7ef3-5061-4a11-b96b-2b7cd110f7b8"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

        input = raw_input("What do you want to tell me? > ")

recognized = classify(input(">")) 

label = recognized["class_name"] 
if label == "Kind_Things":
    print("You're so nice!")
    print(":)")
else:
    print("You're so mean!")
    print(":(")
