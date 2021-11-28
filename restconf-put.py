import json
import requests
requests.packages.urllib3.disable_warnings()

# Variable
api_url = "https://10.10.20.48/restconf//data/ietf-interfaces:interfaces/interface=Loopback2"

# Dictionary variable 
headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

# basicauth = ("cisco", "cisco123!")
basicauth = ("developer", "C1sco12345")

# yangConfig variable 
yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback2",
        "description": "My second RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.2.1.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

# Rest_Put()
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

'''Enter the code below to handle the response. If the response is one of the HTTP success messages, the first message will be printed. Any other code value is considered an error. The response code and error message will be printed in the event that an error has been detected.'''
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))