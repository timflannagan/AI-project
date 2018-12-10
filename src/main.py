'''
https://itnext.io/building-a-chatbot-with-rasa-9c3f3c6ad64d
'''
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy

def run(serve_forever=True):
    interpreter = Interpreter.load("./rasa/data/models/current/default/current")

    while True:
        user_input = raw_input('> ')
        processed_result = interpreter.parse(user_input)
        print(json.dumps(processed_result, indent = 2))

if __name__ == '__main__':
    agent = Agent.load('./rasa/data/models/current/default/current')

    while True:
        user_input = raw_input('> ')

        if 'exit' in user_input:
            break

        responses = agent.handle_message(user_input)

        for response in responses:
            print(response)
