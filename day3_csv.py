#csv 

import csv

f1= open("data1.csv")
type(f1)

csvreader  = csv.reader(f1)
header= []
header = next(csvreader)
print(header)

rows = []
for row in csvreader:
    rows.append(row)
print(rows)


#examples
import csv
rows = []
with open("data1.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

#examples
with open("data1.csv", 'r') as file:
    con = file.readlines()

header = con[:1]
rows = con[1:]
print(header)
print(rows)