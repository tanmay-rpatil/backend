import csv 
data = []

with open('./accel-converted.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	i=0
	for row in reader:
		data.append(row)

for row in data:
	print(row)