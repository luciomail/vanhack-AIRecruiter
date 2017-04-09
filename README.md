# vanhack-AIRecruiter
An Application that collect a job's database and try to infer potencial candidates for the job


Author: Lucio Ribeiro
Operation System: Windows

Instalação:
1. Instale o Python 3
2. Instale os seguintes componentes do Python
	- Redis
	- Flask
	- Requests
3. Instale o servidor Redis
	Windows: https://github.com/MSOpenTech/redis/releases

4. Sugestão de IDE: PyCharm Community


Executando a aplicação:
1. Execute o Servidor Redis
	redis-server.exe
	
2. Rode o WebService
	python webservice/webservice.py

2. Chame o serviço
	- Limpa a base de dados
	curl -i -X POST -H "Content-Type:application/json" http://localhost:5000/bayes/v1.0/reset -d '{"namespace": 0}'

	- Treina a Máquina de inteligência
	curl -i -X POST -H "Content-Type:application/json" http://localhost:5000/bayes/v1.0/learn -d '{"namespace": 0}'

	- Classificar os candidatos e buscar os indicados para uma Empresa específica
	curl -i -X POST -H "Content-Type:application/json" http://localhost:5000/bayes/v1.0/classify -d '{"namespace": 0, "company": "Vanhack"}'

