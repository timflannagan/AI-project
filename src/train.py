from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import warnings

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer

# from rasa_core import utils
# from rasa_core.agent import Agent
# from rasa_core.policies.keras_policy import KerasPolicy
# from rasa_core.policies.memoization import MemoizationPolicy

def train():
    data_location = load_data('./rasa/nlu.md')
    trainer = Trainer(config.load('./rasa/nlu_config.yml'))

    trainer.train(data_location)
    model_directory = trainer.persist('./rasa/data/models/current/', fixed_model_name="current")

    return model_directory

if __name__ == '__main__':
    train()
