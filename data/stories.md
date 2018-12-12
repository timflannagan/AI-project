## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. -->
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. -->
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' -->

## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks

## story_name
* name{"name":"Sam"}
 - utter_greet

## story_query_wiki
* query_wikipedia
 - action_query_wikipedia

## story_get_east_standings
* query_east_standings
 - action_get_east_standings
