from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import logging

def get_response(message):
    chatbot=ChatBot('Dbot',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                logic_adapters=[
            
                {
                "import_path": "chatterbot.logic.BestMatch",
                'maximum_similarity_threshold': 0.90
                ,
                "default_response": 'I am sorry, but I do not understand.',
                },
                ],
                trainer='chatterbot.trainers.ListTrainer')

    while True:
        if message.strip()=='hi':
            return("Hello,I am Dbot a diabetes doctor chatbot.")
            
        if message.strip()!='bye' and message.strip()!='hi':
            reply=chatbot.get_response(message)
            response=str(reply)
            return(response)
        
        if message.strip()=='bye':
            return("bye")
            break



    