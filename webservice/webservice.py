# -*- coding: utf-8 -*-
#!flask/bin/python

from flask import Flask, jsonify, abort, request, make_response, g
from tokenizer.list_tokenizer import ListTokenizer
from store.redis_store_bayes import RedisStoreBayes
from store.redis_store_key_manyValues import RedisStoreKeyManyValues
from bayes.classifier import Classifier
from bayes.naive_bayes import NaiveBayes
import redis
import time
import traceback
import csv
app = Flask(__name__, static_url_path = "")

app.databaseBayes = RedisStoreBayes('localhost', 6379, 0)
app.databasePositionCompanies = RedisStoreKeyManyValues('localhost', 6379, 1)
app.databaseCompaniesToCandidates = RedisStoreKeyManyValues('localhost', 6379, 2)
app.databaseCompanies = RedisStoreKeyManyValues('localhost', 6379, 3)


authorized = ['127.0.0.1']

@app.before_request
def before_request():
    g.start = time.time()

@app.teardown_request
def teardown_request(exception=None):
    diff = int((time.time() - g.start) * 1000)
    print ("Exec time: %s ms" % str(diff))

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(401)
def not_found(error):
    return make_response(jsonify( { 'error': 'Access denied' } ), 401)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.errorhandler(500)
def not_found(error):
    #print error
    print (traceback.print_exc())
    return make_response(jsonify( { 'error': 'Error 500' } ), 500)

# Bayes

@app.route('/bayes/v1.0/learn', methods = ['POST'])
def learn():
    #print('aprendendo...')
    if request.remote_addr not in authorized:
        abort(401)
    if not request.json:
        abort(400)

    tokenizer = ListTokenizer()
    cl = Classifier(tokenizer, app.databaseBayes)
    #app.databasePositionCompanies = RedisStoreCompany('localhost', 6379, 1)

    print('Reading and analysing Jobs'' database.')
    with open('../database/jobs-base.csv', 'r', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        #next(csvreader)

        for row in csvreader:
            cl.train(['cd_skill-' + row[6], 'cd_skill-' + row[8]], 'position-' + row[2] + '(' + row[3] + ')')
            #print('cd_skill-' + row[6] + ' cd_skill-' + row[8] + ' position-' + row[2] + ' company-' + row[4])

            app.databasePositionCompanies.set('position-' + row[2] + '(' + row[3] + ')', 'company-' + row[4])
            app.databaseCompanies.set(row[4], row[5])

    #print(databaseEmpresas.values('position-111'))

    return jsonify( { 'success': True } ), 200

@app.route('/bayes/v1.0/classify', methods = ['POST'])
def classify():
    if request.remote_addr not in authorized:
	    abort (401)
    if not request.json:
        abort(400)

    tokenizer = ListTokenizer()

    if not 'default' in request.json:
        request.json['default'] = 'INDIFERENTE'
    cl = NaiveBayes(tokenizer, app.databaseBayes)
    #cl.setthreshold('C# Senior Web Developer', 2.5)
    #cl.setthreshold('Front End Developer', 2.5)
    #if 'thresholds' in request.json:
        #for threshold in thresholds:
            #cl.setthreshold(key(threshold), value(threshold))

    print('Reading candidates''s database to find best options to company ' + request.json['company-id'] + '...')
    with open('../database/candidato-base500.csv', 'r', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        idUser = 0
        list = []

        for row in csvreader:
            idUserFor = row[0] + ' - ' + row[1]

            if idUser == 0:
                idUser = idUserFor

            if idUser != idUserFor:
                r = cl.classify(list, request.json['default'])
                companies = app.databasePositionCompanies.values(r)

                for comp in companies:
                    #print('company: ' + comp + ' candidate: ' +  idUser + '(' + r + ')')
                    app.databaseCompaniesToCandidates.set(comp, idUser + '(' + r + ')')

                idUser = idUserFor
                list = []

            list.append('cd_skill-' + row[6])

    result = app.databaseCompaniesToCandidates.values('company-' + request.json['company-id'])
    print(result)

    companyName = app.databaseCompanies.values(request.json['company-id'])

    return jsonify( { 'success': True, 'company': companyName, 'result': result} ), 200

@app.route('/bayes/v1.0/reset', methods = ['POST'])
def reset():
    if request.remote_addr not in authorized:
	    abort (401)
    if not request.json:
        abort(400)
    if not 'storeAdress' in request.json:
        request.json['storeAdress'] = 'localhost'
    cl = Classifier(ListTokenizer(), app.databaseBayes)
    cl.store.flush()

    app.databasePositionCompanies.flush()
    app.databaseCompaniesToCandidates.flush()
    app.databaseCompanies.flush()

    return jsonify( { 'success': True } ), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug = False)
