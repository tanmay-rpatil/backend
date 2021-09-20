import csv,json,requests
from typing import OrderedDict 
from time import sleep
# max_row = [10,50,100,500,1000,5000,10000]

def testHelper(request_body):
	r = requests.post(url='http://127.0.0.1:8000/api/insert/', json=request_body)
	return r
