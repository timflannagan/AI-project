from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
import wikipedia
import nba_py
import timeit

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
        dispatcher.utter_message('Sending out a GET request to get the scoreboard for today\`s date. This while take a while.')

        try:
            scoreboard = nba_py.Scoreboard(month=12, day=12, year=2018, league_id='00', offset=0)
            ### To-Do: timeout constructor when time MAX_TIME is reached
        except:
            dispatcher.utter_message('Request took too long to complete. Passing an exception!')
            pass

        return []

class ActionGetWestStandings(Action):
    def name(self):
        return "action_get_west_standings"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Sending out a GET request to get the scoreboard for today\`s date. This while take a while.')

        try:
            scoreboard = nba_py.Scoreboard(month=12, day=12, year=2018, league_id='00', offset=0)
            ### To-Do: timeout constructor when time MAX_TIME is reached
        except:
            dispatcher.utter_message('Request took too long to complete. Passing an exception!')
            pass

        return []

class ActionGetLeagueLeaders(Action):
    def name(self):
        return "action_get_league_leaders"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('getting league leader stats is current a stub.')
        return []

class ActionGetTeamNextGame(Action):
    def name(self):
        return "action_team_next_game"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('getting a team\'s next game is current a stub.')
        return []
