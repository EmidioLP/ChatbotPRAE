#Imports necessários
from datetime import datetime

#Criação da classe para salva o feedback dos usuários
class Log:
    def __init__(self):
        pass
    def saveConversations(self, sessionID, usermessage, intent, botmessage,  dbConn):
        
        #Para formatar a data em qual o feedback foi enviado
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S") 
        
        #Salvar as informações na forma de um arquivo JSON
        mydict = {"sessionID":sessionID,"User Intent" : intent ,"User": usermessage, "Bot": botmessage, "Date": str(self.date) + "/" + str(self.current_time)}

        # Em records fazemos referência a coleção do banco de dados aonde os dados ficarão salvos
        records = dbConn.feedback_records
        records.insert_one(mydict)
