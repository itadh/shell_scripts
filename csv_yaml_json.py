#!/usr/bin/python3

import json, csv

csv_file='/tmp/user.csv'
json_file='/tmp/user.json'
yaml_file='/tmp/user.yml'

data = list()
with open (csv_file) as  csv_fh:
    csv_reader = csv.DictReader(csv_fh, delimiter=';')
    data = list(csv_reader)
#    for rows in csv_reader:
#        print(f'Zeile: {rows}')
#        id = rows['uid']
#        data[id] = rows
#
#with open (json_file) as json_fh:
#    json_fh.write(json.dumps(data, indent=4))

#file = open("/tmp/user.csv", "r")

#dict_reader = csv.DictReader(file, delimiter=';')


#dict_from_csv = list(dict_reader)

json_from_csv = json.dumps(data)


print(json_from_csv)

