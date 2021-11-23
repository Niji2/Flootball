import json
from json.encoder import py_encode_basestring
import time
import os.path
import random
from types import CodeType, GeneratorType

#seed for the RNG
s1, s2, s3 = 169, 420, 808

#RNG, not sure how it works. Will be called many times so I’m happy with how it works. Is predictable if someone figures it out however.
def RNG():
    global s1, s2, s3
    s1 = (171 * s1) %  30269
    s2 = (171 * s2) %  30307
    s3 = (171 * s3) %  30323
    return (s1/30269 + s2/30307 + s3/30323) % 1.0 

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
        currentGame["fspot"] = 50
    else:
        currentGame["fspot"] = 'M',"M","M"
    return currentGame

# this first part acts as an adress book to the correct function for the play, wiht the specific plays shown down below.
def UpdateGameState(teams, owner, theif, score, fspot, downs, yrdsToFirst):
    if(type.downs == int ):
        if(downs == 4 & random.randint(0,4) > 1):
            if(fspot > 51):
                FGBall(teams, owner, theif, score, fspot, downs, yrdsToFirst)
            else:
                PuntBall(teams, owner, theif, score, fspot, downs, yrdsToFirst)
        else:
            if(random.randint(0,1) == 0):
                ThrowBall(teams, owner, theif, score, fspot, downs, yrdsToFirst)
            else:
                RunBall(teams, owner, theif, score, fspot, downs, yrdsToFirst)
    else:
        if(fspot[1] == "M"):
            if(random.randomint(0,1) == 0):
                PassBall(teams, owner, theif, score, fspot, downs, yrdsToFirst)
            else:
                DribbleBall(teams, owner, theif, score, fspot, downs, yrdsToFirst)
        elif(fspot[2] == "M"):
            i = random.randomint(0,100)
            if(i > 90):
                ShootGoal(teams, owner, theif, score, fspot, downs, yrdsToFirst)
            elif(i > 45):
                PassBall(teams, owner, theif, score, fspot, downs, yrdsToFirst)
            else:
                DribbleBall(teams, owner, theif, score, fspot, downs, yrdsToFirst)
        else:
            i = random.randomint(0,50)
            if(i > 25):
                ShootGoal(teams, owner, theif, score, fspot, downs, yrdsToFirst)
            else:
                PassBall(teams, owner, theif, score, fspot, downs, yrdsToFirst)
            
        
    return teams, owner, theif, score, fspot, downs, yrdsToFirst


def RotatePlayers(team, position, player):
    end = player
    teamf = team
    i = 0
    for key in list(team[position]):
        teamf[position][key - 1] = team[position][key]
        i = i + 1
    teamf[position][i] = end
    return teamf


def ThrowBall(teams, owner, theif, score, fspot, downs, yrdsToFirst):
    QB = owner["QB"][1]
    hLB = owner["DEF"][1]
    dLB = theif["DEF"][1]
    dSAF = theif["DEF"][2]
    WR = owner["WR"][1]
    yards = SackCheck(QB, hLB, dLB)
    if(yards == 0):
        resu = ThrowCheck(QB, WR, dSAF)
        if(resu == 0):
            yards = random.randint(1,30)
            yrdsToFirst = yrdsToFirst - yards
            if(yrdsToFirst <= 0):
                downs = 1
            else:
                downs = downs + 1
                if(downs > 4):
                    owner, theif, fspot, downs, yrdsToFirst = ChangeSide(owner, theif, fspot, downs, yrdsToFirst)
        elif(resu == 1):
            downs = downs + 1
            if(downs > 4):
                owner, theif, fspot, downs, yrdsToFirst = ChangeSide(owner, theif, fspot, downs, yrdsToFirst)
        else:
            owner, theif, fspot, downs, yrdsToFirst = ChangeSide(owner, theif, fspot, downs, yrdsToFirst)
    else:
        fspot = fspot - yards
        yrdsToFirst = yrdsToFirst + yards

    owner = RotatePlayers(owner, "QB", QB)
    theif = RotatePlayers(theif, "DEF", dLB)
    theif = RotatePlayers(theif, "DEF", dSAF)
    owner = RotatePlayers(owner, "DEF", hLB)
    owner = RotatePlayers(owner, "WR", WR)
    return teams, owner, theif, score, fspot, downs, yrdsToFirst

def RunBall(teams, owner, theif, score, fspot, downs, yrdsToFirst):
    QB = owner["QB"][1]
    hLB = owner["DEF"][1]
    dLB = theif["DEF"][1]
    dSAF = theif["DEF"][2]
    RB = owner["RB"][1]
    yards = SackCheck(QB, hLB, dLB)
    if(yards == 0):
        yards = RunCheck(RB, dLB)
        fspot = fspot + yards
        yrdsToFirst = yrdsToFirst - yards
    else:
        fspot = fspot - yards
        yrdsToFirst = yrdsToFirst + yards
    
    if(yrdsToFirst <= 0):
        downs = 0
    else:
        if(downs > 4):
            owner, theif, fspot, downs, yrdsToFirst = ChangeSide(owner, theif, fspot, downs, yrdsToFirst)
        else:
            downs = downs + 1
    

    return teams, owner, theif, score, fspot, downs, yrdsToFirst

def PuntBall(teams, owner, theif, score, fspot, downs, yrdsToFirst):
    return teams, owner, theif, score, fspot, downs, yrdsToFirst
def FGBall(teams, owner, theif, score, fspot, downs, yrdsToFirst):
    return teams, owner, theif, score, fspot, downs, yrdsToFirst

def ChangeSide(owner, theif, fspot, downs, yrdsToFirst):
    downs = 1
    fspot = 100 - fspot
    yrdsToFirst = 10
    temp1 = owner
    temp2 = theif
    owner = temp2
    theif = temp1
    return owner, theif, fspot, downs, yrdsToFirst
    




# check designs.
# I want RNG to be invovled, but mostly be based on player stats.
# Total of OFF stats - DEF stats, rng has to roll below to succeed?
# might work.
# time to test

# I FIGURED IT OUT
# THE STATS ARE RANDOMLY USED
# HOLY SHIT
# IF THEY ARE RANDOM
# NO ONE WILL BE ABLE TO FIGURE IT OUT
# YES
# I AM AMAZING

#outputs 0 = not sacked other = how many yards sacked for.
def SackCheck(qb, hDEF, aDEF):
    # gotta love these temp variables.
    #these are all random. they mean nothing. pain.
    a = random.randint(1,9)
    b = random.randint(1,9)
    c = random.randint(1,9)
    d = random.randint(1,9)
    e = random.randint(1,9)
    f = random.randint(1,9)
    bar1 = hDEF[a] + hDEF[b] - aDEF[c]
    check1 = RNG()
    #check if Offensive LB can beat defense LB
    if bar1 < check1:
        return 0
    else:
        bar2 = qb[d] + qb[e] - aDEF[f]
        check2 = RNG()
        # check if QB can out play offensive LB
        if bar2 < check2:
            return 0
        else:
            return round((((1 - check1) + (1 - check2))*4))

#outputs: 0 = caught 1 = missed 2 = intercepted
def ThrowCheck(qb, wr, DEF):
    a = random.randint(1,9)
    b = random.randint(1,9)
    c = random.randint(1,9)
    d = random.randint(1,9)
    e = random.randint(1,9)
    f = random.randint(1,9)
    g = random.randint(1,9)
    h = random.randint(1,9)
    #Check if throw makes it to target
    bar1 = (qb[a] + qb[b]/2)
    if bar1 < RNG():
        #check if throw is caught
        bar2 = wr[c] + wr[d] - DEF[e]
        if bar2 < RNG():
            return 0
        else:
            #check if interception
            bar3 = DEF[f] + DEF[g] - (wr[h]/2)
            if bar3 < RNG():
                return 2
            else: return 1
    else: return 1

# outputs: yards ran.
def RunCheck(rb, DEF):
    a = random.randint(1,9)
    b = random.randint(1,9)
    c = random.randint(1,9)
    d = random.randint(1,9)
    e = random.randint(1,9)
    f = random.randint(1,9)
    g = random.randint(1,9)
    h = random.randint(1,9)
    j = random.randint(1,9)
    i = random.randint(1,9)
    k = random.randint(1,9)
    #check if run is stopeed before line of scrimage
    bar1 = (rb[a] + rb[b]*2) - DEF[c]
    if bar1 < RNG():
        #check if run makes it 1-5 yards
        bar2 = rb[d] + rb[e] - DEF[f]
        if bar2 < RNG():
            #check if run makes 5-15 yard
            bar3 = (rb[g]*2) - DEF[h]
            if bar3 < RNG():
                #check if run makes 15-30 yards
                bar4 = rb[i] - DEF[j]
                if bar4 < RNG():
                    #check if run makes it all da way
                    bar5 = rb[k]/2
                    if bar5 < RNG():
                        return 100
                else:
                    return random.randint(15,30)
            else: return random.randint(5,15)
        else: return random.randint(0,5)
    else: return random.randint(-5,-1)

#outputs: 0 = miss & turnover 1 = made it.
def KickCheck(qb, hDEF, aDEF, yards):
    a = random.randint(1,9)
    b = random.randint(1,9)
    c = random.randint(1,9)
    d = random.randint(1,9)
    e = random.randint(1,9)
    f = random.randint(1,9)
    g = random.randint(1,9)
    #check if fieldgoal is blocked
    bar1 = hDEF[a] + hDEF[b] + hDEF[c] - aDEF[d]
    check1= RNG()
    if bar1 < check1:
        #check if kick is good
        bar2 = (qb[e] + qb[f] + qb[g] - (RNG()))
        check2 = RNG()
        if bar2 < check2:
            return 1
        else: 
            return 0
    else: 
        return 0
# alright, it's time to write down the soccer positions in here.
#    AG   AM   MM   HM   HG
# R  RAG  RAM  RMM  RHM  RHG
# M  MAG  MAM  MMM  MHM  MHG
# L  LAG  LAM  LMM  LHM  LHG
# These are the 15 true states of sloccer. use these as you will
# the ball can only move from the position its in the one of the surrounding positions normally. Goals can be kicked from that sides xM or xG positions, with a penalty 
# if from the xM position, and also if not kicked from MxM/G
# so the flow chart needs to check position, realize where it is, then realize whats around it.
# Passes can go any direction, dribbles can only go forward or diagnaly forward.
# Positions: 
# QB = Goalie
# WR = attackers (xM/xG)
# RB/TE = mid  (xM/MM/xM)
# Saftey/LB = defenders (xM/xG)

def PassBall(teams, owner, theif, score, fspot, downs, yrdsToFirst):
    return teams, owner, theif, score, fspot, downs, yrdsToFirst
def DribbleBall(teams, owner, theif, score, fspot, downs, yrdsToFirst):
    return teams, owner, theif, score, fspot, downs, yrdsToFirst
def ShootGoal(teams, owner, theif, score, fspot, downs, yrdsToFirst):
    return teams, owner, theif, score, fspot, downs, yrdsToFirst


def ChangeGame(downs, fspot, teams, owner):
    if(downs > 0):
        downs = 1
        if(teams[1] == owner):
            if(fspot < 20):
                fspot = 'M', 'H', 'G'
            elif(fspot < 40):
                fspot = 'M', 'H', 'M'
            elif(fspot < 60):
                fspot = 'M', 'M', 'M'
            elif(fspot < 80):
                fspot = 'M', 'A', 'M'
            else:
                fspot = 'M', 'A', 'G'
        else:
            if(fspot < 20):
                fspot = 'M', 'A', 'G'
            elif(fspot < 40):
                fspot = 'M', 'A', 'M'
            elif(fspot < 60):
                fspot = 'M', 'M', 'M'
            elif(fspot < 80):
                fspot = 'M', 'H', 'M'
            else:
                fspot = 'M', 'H', 'G'
    else:
        downs = 0
        if(teams[1] == owner):
            if(fspot[2] == "G" & fspot[1] == "H"):
               fspot = 20 
            elif(fspot[2] == "G" & fspot[1] == "A"):
                fspot = 80
            elif(fspot[2] == "M" & fspot[1] == "H"):
                fspot = 40
            elif(fspot[2] == "M" & fspot[1] == "A"):
                fspot = 60
            else:
                fspot = 50
        if(random.randint(0,1) == 1):
            fspot = fspot + random.randint(0,10)
        else:
            fspot = fspot - random.randint(0,10)
    return downs, fspot



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