'''
https://itnext.io/building-a-chatbot-with-rasa-9c3f3c6ad64d
'''
from rasa_nlu.model import Metadata, Interpreter

import logging
import json

def run(serve_forever=True):
    interpreter = Interpreter.load("./rasa/data/models/current/default/current")

    while True:
        user_input = raw_input('> ')
        processed_result = interpreter.parse(user_input)
        print(json.dumps(processed_result, indent = 2))

if __name__ == '__main__':
    run()
