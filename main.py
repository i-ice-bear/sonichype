import spacy
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import languages
from chatterbot import ChatBot


nlp = spacy.load("en_core_web_sm")
chatbot = ChatBot("Chatpot")

exit_conditions = (":quit", ":exit")

while True:
    __user__input__query = input(" > ")
    if __user__input__query in exit_conditions:
        break
    else:
        print(f" Entered : {chatbot.get_response(__user__input__query)} ")