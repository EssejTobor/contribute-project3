import os
import csv
import json



csvFilePath = r'C:\Users\Jesse\Desktop\WebStudys\JavaScript\homework\Project 3\Trial 1\assets\data\world-country-names.csv'
jsonFilePath = r'C:\Users\Jesse\Desktop\WebStudys\JavaScript\homework\Project 3\Trial 1\assets\data\world-country-names.json' 


data = {}
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows ['id']
        data[id] = rows


with open(jsonFilePath, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=4))
