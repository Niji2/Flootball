import json
from json.encoder import py_encode_basestring
import time
import os.path
import random
from types import CodeType

#Starting point for each game, with starting style randomly decided
baseGame = {
    "teams": {1:None, 2:None},
    "owner": None,
    "Theif": None,
    "score": {1:0, 2:0},
    "fSpot": 50,
    "downs": 1,
    "yrdsTofirst": 10
}

currentGame = baseGame
#Oh boy here we go
#First the GetGameState Function, we first check if the game exists. IF it doesn't we make the game exsist and we start it.
def GetGameState():
    #Does Game Exist?
    if(os.path.exists("game.json")):
        with open("game.json", "r") as read:
            Game = json.load(read)
        teams = Game["teams"]
        owner = Game["owner"]
        theif = Game["Theif"]
        score = Game["Score"]
        fSpot = Game["fSpot"]
        downs = Game["downs"]
        yrdsToFirst = Game["yrdsToFirst"]
        return teams, owner, theif, score, fSpot, downs, yrdsToFirst
    else:
        #Make The Game!
        Game = StartGame()
        with open("game.json","w") as game_write:
            json.dump(Game)
        #Game should now be in json file, ready to be started
        with open("game.json", "r") as read:
            Game = json.load(read)
        teams = Game["teams"]
        owner = Game["owner"]
        theif = Game["Theif"]
        score = Game["Score"]
        fSpot = Game["fSpot"]
        downs = Game["downs"]
        yrdsToFirst = Game["yrdsToFirst"]
        return teams, owner, theif, score, fSpot, downs, yrdsToFirst
#Starting a game!
def StartGame():
    #first we declare the teams and add them to the current game
    with open("teams.json","r") as read_teams:
            teams = json.load(read_teams)
    i = 0
    home = teams["Orono Juicers"]
    away = teams["Blue Badgers"]
    for key in teams:
        print(key)
        i = i + 1
        global currentGame
        currentGame["teams"][i] = key
    #now we set Owner and Theif
    currentGame["owner"] = home
    currentGame["Theif"] = away
    #Finally we randomly set game type, int for football, string for soccer
    if(random.randint(0,1) == 1):
        currentGame["downs"] = 1
    else:
        currentGame["downs"] = "MMM"
    return currentGame

# this first part acts as an adress book to the correct function for the play, wiht the specific plays shown down below.
def UpdateGameState(teams, owner, theif, score, fSpot, downs, yrdsToFirst):
    if(type.downs < int ):
        if(downs == 4 & random.randint(0,4) > 1):
            if(fSpot > 51):
                FGBall()
            else:
                PuntBall()
        else:
            if(random.randint(0,1) == 0):
                ThrowBall()
            else:
                RunBall()
    else:
        no = no
        
    return teams, owner, theif, score, fSpot, downs, yrdsToFirst


def ThrowBall():
    return no

def RunBall():
    return no

def PuntBall():
    return no
def FGBall():
    return no

# alright, it's time to write down the soccer positions in here.
#    AG   AM    MM   HM   HG
# R  RAG  RAM  RMM  RHM  RHG
# M  MAG  MAM  MMM  MHM  MHG
# L  LAG  LAM  LMM  LHM  LHG
# These are the 15 true states of sloccer. use these as you will
# the ball can only move from the position its in the one of the surrounding positions normally. Goals can be kicked from that sides xM or xG positions, with a penalty 
#if from the xM position, and also if not kicked from MxM/G
# so the flow chart needs to check position, realize where it is, then realize whats around it.

def SetGameState(teams, owner, theif, score, fSpot, downs, yrdsToFirst):
    with open("game.json", "r") as read:
            Game = json.load(read)
    Game["teams"] = teams
    Game["owner"] = owner
    Game["Theif"] = theif
    Game["score"] = score
    Game["fSpot"] = fSpot
    Game["downs"] = downs
    Game["trdsToFirst"] = yrdsToFirst
    with open("game.json", "w") as write:
        json.dump(Game)
    return


def PlayBall():
    teams, owner, theif, score, fSpot, downs, yrdsToFirst = GetGameState(baseGame)
    teams, owner, theif, score, fSpot, downs, yrdsToFirst = UpdateGameState(teams, owner, theif, score, fSpot, downs, yrdsToFirst)
    SetGameState(teams, owner, theif, score, fSpot, downs, yrdsToFirst)



#while (1 == 1):
    #time.sleep(5)
    #PlayBall()