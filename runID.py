import requests
import json

url = "https://companyName.safebreach.com/api/config/v1/accounts/<accountId>/schedules?details=<boolean>&deleted=<boolean>"

payload = {}
headers = {
  'Accept': 'application/json',
  'x-apitoken': '{{api_token}}',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
