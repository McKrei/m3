import csv

with open('data.csv', newline='') as file:
    data = csv.reader(file, delimiter='|')
    print(type(data))
    for line in data:
        print(line)
