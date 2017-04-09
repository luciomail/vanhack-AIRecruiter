#!/usr/bin/env python

import requests
from datetime import datetime

def trainws():
	r = requests.post("http://localhost:5000/bayes/v1.0/reset", json={"namespace": 0})
	r = requests.post("http://localhost:5000/bayes/v1.0/learn",
						json={"namespace": 0})

def classifyws():
	print('Searching candidates...')

	#calling service for Vanhack (company-id = 1)
	r = requests.post("http://localhost:5000/bayes/v1.0/classify", json={"namespace": 0, "company-id": '1'})

	#calling service for Jostle (company-id = 882)
	#r = requests.post("http://localhost:5000/bayes/v1.0/classify", json={"namespace": 0, "company-id": '881'})

	print(r.text)

def resetws():
	r = requests.post("http://localhost:5000/bayes/v1.0/reset", json={"namespace": 0})
	print(r)


if __name__ == '__main__':
	startTime = datetime.now()
	#resetws()
	trainws()
	classifyws()
	print('Time spent: ' + str(datetime.now() - startTime))
