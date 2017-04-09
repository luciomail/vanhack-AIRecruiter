# vanhack-AIRecruiter
An Application that collects two databases (one of jobs and another of candidates) and try to infer potencial candidates for the company.
We use Nayve Bayes technique. The application learns about jobs' database of companies and sugests candidates for them.

It's possible to change some parts of the algorithm to your necessity or try to use another algorithm of AI.


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

	- Call the service
		- Using PyCharm
			Open the __main__.py file and Run it (Right button click mouse and Run)
			In the method "classifyws()" you can change de "company-id" and test with another companies (see jobs-base.csv)

		- Using cURL
			- Clear the intelligence machine database
				curl -i -X POST -H "Content-Type: application/json" http://localhost:5000/bayes/v1.0/reset -d '{"namespace": 0}'

			-Train intelligence machine
				curl -i -X POST -H "Content-Type: application/json" http://localhost:5000/bayes/v1.0/learn -d '{"namespace": 0}'

			- Classify the candidates based on their skills and search the ones for a specific company (In this database: Company-Id = 1 for Vanhack)
				curl -i -X POST -H "Content-Type: application/json" http://localhost:5000/bayes/v1.0/classify -d '{"namespace": 0, "company-id": "1"}'



Some important points:
- This example (webservice.py) uses the database "database/candidato-base500". It has a few candidates and their skills. It's a small database. (It will take at about 5 minutes)

- If you want to increase the quantity of candidates, you have to change "webservice.py" and call another database file (database/candidato-base13mil ou database/candidato-base). In this case, the time spent will be much longer.

- In this implementation, we did not focus on performance in generating better the csv format of the file or in reading the file.
