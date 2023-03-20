import csv

with open('data.csv', newline='') as file:
    data = csv.DictReader(file)
    print(data.fieldnames)
    for line in data:
        print(line['name'], line['height'])
['name', 'height', 'mass', 'hair_color', 'skin_color']
Luke Skywalker 172
C-3PO 167
R2-D2 96
Darth Vader 202
Leia Organa 150
Yoda 66