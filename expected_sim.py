import requests
import json

url = "https://companyName.safebreach.com/api/orch/v1/accounts/Value/plan/statistics?limit=500000&includeDisabled=true"

payload = json.dumps({
  "name": "",
  "steps": [
    {
      "attacksFilter": {
        "playbook": {
          "operator": "is",
          "values": [
            2220,
            2268,
            4135,
            2631,
            1224,
            803,
            2611,
            2170,
            2192,
            3671,
            2110,
            2241,
            904,
            2153,
            2244,
            2264,
            1228,
            2213,
            240,
            2332,
            2222,
            2246,
            1011,
            2251,
            2189,
            1695,
            806,
            2247,
            98,
            110,
            122,
            2265,
            1693,
            2294,
            100,
            1220,
            2218,
            2214,
            106,
            2355,
            2278,
            2348,
            4088,
            2173,
            3680,
            2342,
            2243,
            2353,
            810,
            2632,
            2339,
            2346,
            2263,
            2266,
            2236,
            2242,
            823,
            2349,
            1355,
            2187,
            1430,
            2306,
            179,
            176,
            2337,
            2347,
            2221,
            2356,
            2279,
            1698,
            2308,
            2343,
            2608,
            1902,
            2293,
            2344,
            172,
            4222,
            214,
            2612,
            1527,
            112,
            2630,
            131,
            1357,
            4029,
            2194,
            109,
            2239,
            1394,
            2345,
            2302,
            2295,
            1462,
            2248,
            1292,
            4136,
            2219,
            2191,
            133,
            192,
            1269,
            241,
            3820,
            908,
            2188,
            2340,
            2250,
            2217,
            2350,
            1338,
            2273,
            796,
            2267,
            2238,
            2199,
            1377,
            2193,
            2205,
            2357,
            268,
            2341,
            911
          ],
          "name": "playbook"
        }
      },
      "attackerFilter": {
        "simulators": {
          "operator": "is",
          "values": [
            "4a31b868-e069-42f8-9357-64e2260742a2"
          ],
          "name": "simulators"
        }
      },
      "targetFilter": {
        "simulators": {
          "operator": "is",
          "values": [
            "2167e9eb-6a26-438c-814f-23e79a114692",
            "d90fdaf3-5abe-4e6a-a17d-aec69396f7df"
          ],
          "name": "simulators"
        }
      },
      "systemFilter": {
        "bypassProxy": {
          "operator": "is",
          "values": [
            True
          ],
          "name": "bypassproxy"
        },
        "proxies": {
          "operator": "is",
          "values": [],
          "name": "proxies"
        }
      }
    }
  ]
})
headers = {
  'Content-Type': 'application/json',
  'x-apitoken': '{{api_token}}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
