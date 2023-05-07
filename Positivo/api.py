import requests
import json

url = "https://type.fit/api/quotes"

response = requests.get(url)
print(response.text)
result = response.json()
