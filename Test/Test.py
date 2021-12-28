import json
import sys

import requests

baseUrl = "http://test"

r = requests.get(baseUrl + "/sensors.php?id=d72df2d5-61ec-4d88-94d5-658fa603487b")
print(r.status_code)
if r.status_code != 200:
    print("Fehler beim Request")
    print(r.text)
    sys.exit(0)

print(r.text)
data = json.loads(r.text)

for sensor in data["Sensors"]:
    if sensor["dbid"] == "3":
        sensor["value"] = -20
    else:
        sensor["value"] = -20

print("Nach setzen von Messwerten", data)

s = json.dumps(data)
r = requests.post(baseUrl + "/submit.php", s)
if r.status_code != 200:
    print("Fehler beim Request")
    print(r.text)
    sys.exit(0)
print("Antwort vom Server:", r.text)
