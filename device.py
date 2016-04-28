import csv
import json
import requests

with open('devices.csv', "rb") as devices_source:
    reader = csv.reader(devices_source)
    devices = [row for row in reader]

url = 'https://cloudhelix.com/api/v1/device/create'
payload = devices
headers = {"X-CH-Auth-Email": "brandon@brandonbianchi.com",
           "X-CH-Auth-API-Token": "6c079ba92b2a8fe5977519f6859ecf80",
           "Content-Type": "application/json; charset=utf-8"}

response = requests.post(url, data=json.dumps(payload), headers=headers)
print response.content
print devices