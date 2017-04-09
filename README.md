# vanhack-AIRecruiter
An Application that collect a job's database and try to infer potencial candidates for the job

Author: Lucio Ribeiro

Instalation:
1. Install Git and get the project on github
	- Windows: https://git-scm.com/download/win
	- Linux: apt-get install git
	- Project on git hub: https://github.com/luciomail/vanhack-AIRecruiter

2. Install Python 3
	- Windows: https://www.python.org/downloads/release/python-360/
	- Ubuntu: By default, Python is already installed (if necessary, sudo apt-get install python3)

3. Install the IDE: PyCharm Community
	- Windows: https://www.jetbrains.com/pycharm/download
	- Ubuntu: https://www.jetbrains.com/pycharm/download

	Execute the IDE and open the project

4. Install some necessary components of Python
	- Using PyCharm, you can install all the componentes
		- Menu File > Settings
		- Look for Project: vanhack-AIRecruiter
		- In the item Project Iterpreter
			* make sure that Python 3 is set as Project Interpreter
			* install the following components, clicking at plus button
				Redis, requests, flask and setuptools (if it's not installed)


	- You also can install the components using prompt command
		- Redis
			pip3 install redis (Windows e Ubuntu)
		- Flask
			pip3 install redis (Windows e Ubuntu)
		- Requests
			pip3 install requests (Windows e Ubuntu)

4. Install Redis Server
	Windows: https://github.com/MSOpenTech/redis/releases
	Ubuntu: sudo apt-get install redis-server

5. Run the application
	- Run Redis Server
		Windows: redis-server.exe
		Ubuntu: redis-server
	
	- Start the WebService
		- Using PyCharm
			Open the webservice.py file and Run it (Right button click mouse and Run)
		- Using prompt command
			python webservice.py

	- Call the service
		- Using PyCharm
			Open the __main__.py file and Run it (Right button click mouse and Run)
		- Using prompt command
			python __main__.py
		- Using cURL
			- Clear the intelligence machine database
				curl -i -X POST -H "Content-Type: application/json" http://localhost:5000/bayes/v1.0/reset -d '{"namespace": 0}'

			-Train intelligence machine
				curl -i -X POST -H "Content-Type: application/json" http://localhost:5000/bayes/v1.0/learn -d '{"namespace": 0}'

			- Classify the candidates based on their skills and search the ones for a specific company
				curl -i -X POST -H "Content-Type: application/json" http://localhost:5000/bayes/v1.0/classify -d '{"namespace": 0, "company-id": "1"}'

