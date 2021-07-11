from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import logging

def train():
    chatbot=ChatBot('Dbot',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
               
                trainer='chatterbot.trainers.ListTrainer')

    trainer=ListTrainer(chatbot)

    for file in os.listdir('E:/Drbot/bot/Data/'):
            data=open('E:/Drbot/bot/Data/' + file,encoding='latin-1').readlines()   
            trainer.train(data)
    

train()       