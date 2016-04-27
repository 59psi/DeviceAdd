import csv
import json
import urllib2


with open('devices.csv', "rb") as devices_source:
    reader = csv.reader(devices_source)
    devices = [row for row in reader]

data = {"X-CH-Auth-Email": "brandon@brandonbianchi.com",
        "X-CH-Auth-API-Token": "6c079ba92b2a8fe5977519f6859ecf80",
        "devices": devices}

req = urllib2.Request('https://cloudhelix.com/api/v1/device/create')
req.add_header('Content-Type', 'application/json; charset=utf-8')

response = urllib2.urlopen(req, json.dumps(data))
