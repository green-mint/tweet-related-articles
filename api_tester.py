import requests
import sys
import json

args = sys.argv[1:]

query = ""

for arg in args:
    query += arg + " "

complete_URL = "https://twitter-hackathon-api.herokuapp.com/"
# complete_URL = "http://127.0.0.1:5000/"

response = requests.get(complete_URL, params={
    'text': query
})

print(json.dumps(response.json()))
