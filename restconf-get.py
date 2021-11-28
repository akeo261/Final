import json
import requests
requests.packages.urllib3.disable_warnings()

# Variable
api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces"

# Dictionary variable 
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

# basicauth = ("cisco", "cisco123!")
basicauth = ("developer", "C1sco12345")

# Step 3: Create a variable to send the request and store the JSON response.
# requests.get()
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
print(resp)

response_json = resp.json()
#print(response_json)

print(json.dumps(response_json, indent=5))
