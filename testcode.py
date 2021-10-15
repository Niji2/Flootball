import json
import random

baseGame = {
    "teams": {1:None, 2:None},
    "score": {1:0, 2:0},
    "fSpot": 50,
    "downs": random.randint(0,1),
    "yrdsTofirst": 10
}

with open("teams.json","r") as read_teams:
     teams = json.load(read_teams)
home = teams["Orono Juicers"]
away = teams["Blue Badgers"]
print(home)
print(" ")
print(away)
i = 0


print(baseGame)