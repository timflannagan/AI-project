# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
import wikipedia
import nba_py

from rasa_core_sdk import Action

logger = logging.getLogger(__name__)

class ActionQueryWikipedia(Action):
    def name(self):
        return "action_query_wikipedia"

    def run(self, dispatcher, tracker, domain):
        last_message = tracker.current_state()['latest_message']['text']

        try:
            wiki_summary = wikipedia.summary(last_message)
            dispatcher.utter_message(wiki_summary)
        except:
            dispatcher.utter_message('I was not able to find any information on "{}!" Did you misspell a player\'s name?'.format(last_message))
            return []

class ActionGetEastStandings(Action):
    def name(self):
        return "action_get_east_standings"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('getting east standings is currently a stub.')
        return []
