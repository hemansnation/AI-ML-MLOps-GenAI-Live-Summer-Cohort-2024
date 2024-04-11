import requests

url = 'https://us-central1-formidable-rune-420015.cloudfunctions.net/classifier'

a = input("Enter a string: ")

r = requests.post(url, json={
    "model":["DecisionClassifier"],
    "x": [a]
})

print(r.text)