#Importações de bibliotecas necessárias
from cmath import log
import json
from re import fullmatch
from flask import Flask, request, jsonify, render_template, make_response
from flask_cors import CORS, cross_origin
import os
import pymongo
from pymongo import MongoClient
from SaveConversation import Conversations


#Inicializição da aplicação FLASK sob o nome "app"
app = Flask(__name__) 

# Recebendo e enviando respostas para o Dialogflow
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

#Conectando a aplicação a base de dados no MongoDB
def ConfigureDatabase():
    client = MongoClient("mongodb+srv://prae_user:Sua Permissão Aqui")
    return client.get_database('Nome do Banco de Dados')
 
# Processando as requests do Dialogflow
def processRequest(req):
    log = Conversations.Log()
    sessionID = req.get('responseId')
    result = req.get("queryResult")
    intent = result.get("intent").get('displayName')
    query_text = result.get("queryText")
    bot_message = result.get("fulfillmentText")
    parameters = result.get("parameters")
    db = ConfigureDatabase()

    if intent == "[Edital] Duvida - Sim" or intent == "[Edital] Duvida - Nao":
        log.saveConversations(sessionID, query_text, intent, bot_message, db)



#Inicializando a aplicação no servidor
if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
