import csv

f = open('devices.csv')
csv_file = csv.reader(f)

print_device = []
for row in csv_file:
    print_device.append(row[3])

print print_device

f.close()
