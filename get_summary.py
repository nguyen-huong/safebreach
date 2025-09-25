import requests
import json

url = "https://companyName.safebreach.com/api/data/v1/accounts/<accountId>/testsummaries/<string>"

payload = {}
headers = {
  'Accept': 'application/json',
  'x-apitoken': '{{api_token}}',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
