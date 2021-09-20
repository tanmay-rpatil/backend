from test_insertions import testHelper
from time import sleep
import csv,json,requests
from typing import OrderedDict 
max_row = []
for i in range(4):
	max_row.append(20000)

api_url = 'http://127.0.0.1:8000/api/insert/'
with open('./Sample_Data/accel-converted.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for count in max_row:
		request_body = OrderedDict()
		data = []
		i = 0
		for row in reader:
			data.append(row)
			i += 1
			if(i>=count):
				break
		request_body['sensor_id'] = 1
		request_body['data'] = data
		request_body['count'] = count
		# print(json.dumps(request_body))
		testHelper(request_body)
		sleep(1)