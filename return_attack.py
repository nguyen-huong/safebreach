import requests
import json

url = "https://companyName.safebreach.com/api/content/v3/accounts/<integer>/moves?source=<string>&moveId=<integer>&deleted=<boolean>"

payload = {}
headers = {
  'Accept': 'application/json',
  'x-apitoken': '{{api_token}}',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
