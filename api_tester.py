import requests
import sys

args = sys.argv[1:]

query = ""

for arg in args:
    query += arg + " "

complete_URL = "http://localhost:5000/"

response = requests.get(complete_URL, params={
    'text': query
})

print(response.json())
