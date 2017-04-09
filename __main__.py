#!/usr/bin/env python

import requests
from datetime import datetime

def trainws():
	print(requests.post("http://localhost:5000/bayes/v1.0/reset", json={"namespace": 0}))
	print(requests.post("http://localhost:5000/bayes/v1.0/learn",
						json={"namespace": 0}))

def classifyws():
	r = requests.post("http://localhost:5000/bayes/v1.0/classify", json={"namespace": 0, "company": "Vanhack"})
	print(r.text)

def resetws():
	r = requests.post("http://localhost:5000/bayes/v1.0/reset", json={"namespace": 0})
	print(r)


if __name__ == '__main__':
	startTime = datetime.now()
	#resetws()
	trainws()
	classifyws()
	print('Tempo de execução: ' + str(datetime.now() - startTime))
