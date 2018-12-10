from rasa_core_sdk import Action

class ActionGetWikipediaPlayerInfo:
    def name(self):
        return "return_wiki_info"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_query_wikipedia")
        return []
