## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks

## story_query_wiki
* query_wikipedia
 - action_query_wikipedia

## story_get_east_standings
* query_east_standings
 - action_get_east_standings

## story_get_west_standings
* query_west_standings
 - action_get_west_standings

## story_get_league_leaders
* query_league_leaders
 - action_get_league_leaders

## story_get_team_next_game
* query_team_next_game:
 - action_get_team_next_game
## Generated Story 145461282119993777
* query_team_next_game{"team": "celtics"}
    - action_get_team_next_game
* query_team_next_game{"team": "bucks"}
    - action_get_team_next_game
    - utter_greet
* query_wikipedia{"player": "boston celtics"}
    - slot{"player": "boston celtics"}
    - action_query_wikipedia
* goodbye{"goodbye": "bye"}
    - utter_goodbye
    - action_default_fallback
    - rewind

