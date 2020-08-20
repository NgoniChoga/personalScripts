import json 
import requests
from requests.auth import HTTPBasicAuth

url = ""
filename = "ids.txt"

big_json = {"metadata":""}
metadata = "{{\"workflow\":\"uct-include-tag\",\"configuration\":{}}}"

with open(filename) as f:
    mylist = f.read().splitlines()
    all_config = {}
    for x in mylist:
        all_config[x] = {}
    
    metadata = metadata.format(json.dumps(all_config))

big_json["metadata"] = metadata

print(big_json)

response = requests.post(url + '/admin-ng/tasks/new', data=big_json, auth=HTTPBasicAuth('user', 'pass'))
print(response.text)