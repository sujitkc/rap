import os
import csv
import random

# To extract pattern of the existing data

fileName = "review-panels.csv"
if (not os.path.isfile(fileName)):
    print(fileName + ": file does not exist.")
data = open(fileName, "r")
csvData = csv.reader(data)
prof = []

for row in csvData:
    for i in range(len(row)-1):
		if(row[i + 1] not in prof):
			prof.append(row[i + 1])
prof_dict = {}
for d in prof:
    prof_dict[d] = 0;

for row in csvData:
    for i in range(len(row) - 1):
        prof_dict[row[i + 1]] = prof_dict[row[i + 1]] + 1

#print(prof_dict)