from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

if __name__ == '__main__':

    agent = Agent(, policies=[MemoizationPolicy(max_history=3),KerasPolicy()],
                interpreter='./models/current/nlu')

    training_data = agent.load_data(training_data_file)

    agent.train_online(
        training_data,
        epochs=400,
        batch_size=100,
        validation_split=0.2)
