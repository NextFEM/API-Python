import requests
from pathlib import Path
import os; import json

base_url = "http://localhost:5151"
username = "yourUserName"; # needed only if you're using a public NextFEM API server

def NextFEMapi(method, command, user, body=None):
    global base_url
    url = base_url + command
    headers = {"user": user}
    if method == "POST":
        response = requests.post(url=url, headers=headers, json=body)
    elif method == "PUT":
        response = requests.put(url=url, headers=headers, json=body)
    elif method == "GET":
        response = requests.get(url=url, headers=headers)
    elif method == "DELETE":
        response = requests.delete(url=url, headers=headers)
    # print type, path and response
    print("*** " + user + " :: " + method, command, response.status_code)
    return response.text

# current dir
dir = os.path.dirname(os.path.realpath(__file__))

# version
print("NextFEM API version: " + NextFEMapi("GET", "/version",username))
print("New model: " + NextFEMapi("GET", "/op/new",username))
# send model
with open(dir + r"\sample.json") as f:
    contents = json.load(f)
print("Send model: " + NextFEMapi("POST","/model/data", username, contents))
# run
print("Run model: " + NextFEMapi("GET","/op/run", username))

if username == "yourUserName":
    # refresh screen - to be used only with local NextFEM Designer program - no username needed
    print("Save model: " + NextFEMapi("GET","/op/view/0/resize", username))
else:
    # save in cloud - to be used only if you're using a public NextFEM API server
    print("Save model: " + NextFEMapi("GET","/op/saveuser", username))

# position of node 1
print("Node 1: " + NextFEMapi("GET","/node/1", username))