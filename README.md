# AI-project:
COMP.4200 Project Repo

### Project Idea:
Create a chatbot that generates relevant NBA information given the user's question.

### Usage:
1. Clone the repo:
```
$ git clone https://github.com/timflannagan1/AI-project
```
2. Run the requirements.txt:
```
$ pip install -r requirements.txt
```
3. Run the python chatbot file:
```
$ python nba_chatbot.py
```

### Expert System Process Flow:
* User enters a command
* The chatbot searches it's `stat` database to find the appropriate stat
* The chatbot then searches `response` database to return the correct response.

### Example endpoint from `stats.nba.com`:
```
stats.nba.com/stats/scoreboard/?GameDate=02/14/2015&LeagueID=00&DayOffset=0
```
