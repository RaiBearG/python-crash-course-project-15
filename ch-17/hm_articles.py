import requests
import json

#make the api call 
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# explorer structure of the data
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)