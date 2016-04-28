import csv
import json
import requests

with open('devices.csv', "rb") as devices_source:
    reader = csv.reader(devices_source)
    devices = [row for row in reader]

url = 'https://cloudhelix.com/api/v1/device/create'
headers = {"X-CH-Auth-Email": "brandon@brandonbianchi.com",
           "X-CH-Auth-API-Token": "6c079ba92b2a8fe5977519f6859ecf80",
           "Content-Type": "application/json; charset=utf-8"}

for device in devices:
    device_name = device[0]
    device_description = device[1]
    type = device[2]
    flow_type = device[3]
    flow_rate = device[4]
    other_ips = device[5]
    somecsv = ",".join(device)
    payload = {
        'device_name': device[0],
        'device_description': device[1],
        'type': device[2],
        'flow_type': device[3],
        'flow_rate': device[4],
        'other_ips': device[5]
    }
    print payload

r = requests.post(url, data=json.dumps(payload), headers=headers)
print r