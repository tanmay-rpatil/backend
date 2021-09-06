import csv,json
from typing import OrderedDict 

data = []
max_row = 10000
request_body = OrderedDict()

with open('./Sample_Data/accel-converted.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	i=0
	for row in reader:
		data.append(row)
		i += 1
		if(i>=max_row):
			break

# print(type(request_body))
# for row in data:
# 	print(row)
request_body['sensor_id'] = 1
request_body['data'] = data
print(json.dumps(request_body))
