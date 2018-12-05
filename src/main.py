'''
https://itnext.io/building-a-chatbot-with-rasa-9c3f3c6ad64d
'''

from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter
import json

def ask_question(text):
    print(json.dumps(interpreter.parse(text), indent=2))

if __name__ == '__main__':
    interpreter = Interpreter.load("../rasa/models/current/nlu")
    ask_question('who is Kyrie Irving?')
    ask_question('who is James Harden?')
