import csv

filename = 'data1.csv'

fields = []
rows = []

with open(filename,'r') as csvfile:
    csvreader = csv.reader(csvfile) ## reader object

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)

    print(f'total number of rows: {csvreader.line_num}') # row count

    print('Field names are: ' + ', '.join(fields))

print('data is as follows')

for row in rows:
    print(row)