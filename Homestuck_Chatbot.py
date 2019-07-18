import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "6a3f1d60-a980-11e9-a5c3-a57241a5ff449cd91a87-488c-4cf1-8441-c2557b5a04a7"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
        
def answer_question():
    question = input(">")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    
    if confidence < 75:
        print("I'm not sure. Ask another question please.")
    elif answerclass == "John":
        print("John Egbert")
    elif answerclass == "Rose":
        print("Rose Lalonde")
    elif answerclass == "Dave":
        print("Dave Strider")
    elif answerclass == "Jade":
        print("Jade Harley")
        
print("What do you want to know about Homestuck?")
while True:
    answer_question()