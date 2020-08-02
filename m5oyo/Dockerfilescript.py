
import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint

#Defines username, password, and URL for auth token
USER = "devnetuser"
PASS = "Cisco123!"
URL = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"



#This code was taken from getDevices.py which was included in Module3
#it was edited to change variables
headers = {'Content-Type': 'application/json'}

body = requests.post(URL, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)

token = body.json()['Token']

print("Your generated token is: " + token)

URL2 = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-health"

getheader = {'Accept': 'application/json', 'X-auth-token': token}

getbody = requests.get(URL2, headers=getheader, verify=False)

forceJSON = getbody.json()

pprint(forceJSON)

#Script pulls Network Health data from DNAC API