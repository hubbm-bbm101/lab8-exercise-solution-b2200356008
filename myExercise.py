import os
import sys

fileName = sys.argv[1]
names = sys.argv[2].split(",")
file = open(fileName)

records = dict()

for line in file:
    temp = line.strip("\n ").split(":")
    name = temp[0]
    records[name] = temp[1]

for name in names:
    try:
        assert name in records
        print("Name: {}, University: {}".format(name, records[name]))
    except:
        print("No record of \'{}\' was found".format(name))

file.close()