import json
import random
#seed for the RNG
s1, s2, s3 = 100, 100, 100

#RNG, not sure how it works. Will be called many times so I’m happy with how it works. Is predictable if someone figures it out however.
def RNG():
    global s1, s2, s3
    s1 = (171 * s1) %  30269
    s2 = (171 * s2) %  30307
    s3 = (171 * s3) %  30323
    return (s1/30269 + s2/30307 + s3/30323) % 1.0 

def NameCreateF():
    i = random.randint(0,100)
    return i

def NameCreateL():
    i = random.randint(0,100)
    return i
#use as (character name) = CharCreate(Character's first name, Character's last name) 
#everything els handled by RNG
def CharCreate():    
    i = {
        "First Name": NameCreateF(),
        "Last Name": NameCreateL(),
        1: RNG(),
        2: RNG(),
        3: RNG(),
        4: RNG(),
        5: RNG(),
        6: RNG(),
        7: RNG(),
        8: RNG(),
        9: RNG(),

        # commenting out below until i figure out what to do with it
        # based sully
        #"Flappability": RNG(),
        #"Aprosexability": RNG(),
        #"Dordbility": RNG(),
        #"Imprigrious": RNG(),
        #"Macilient": RNG(),
        #"Miclewritter": RNG(),
        #"Nittiness": RNG(),
        #"Noceny": RNG(),
        #"Pilliverish": RNG(),
        #"Pyknic": RNG(),
        #"Scibility": RNG(),
        #"Testudineous": RNG(),
        #"Yemeles": RNG(),
        #"Zoilist": RNG(),
        #"Hypersaliant": RNG(),
        #"Overwashed": RNG(),
        #"Segmented": RNG()
    }
    return i
 
Character = CharCreate()

def TeamCreate():
    i2={"QB": {1:CharCreate()},
        "WR":{1:CharCreate(), 2:CharCreate(), 3:CharCreate()},
        "RB":{1:CharCreate(), 2:CharCreate(), 3:CharCreate(), 4:CharCreate(), 5:CharCreate(), 6:CharCreate()},
        "DEF":{1:CharCreate(), 2:CharCreate(), 3:CharCreate(), 4:CharCreate(), 5:CharCreate(), 6:CharCreate(), 7:CharCreate(), 8:CharCreate(), 9:CharCreate()}}
    return i2
teams = {
        "Orono Juicers": TeamCreate(),
        "Blue Badgers": TeamCreate()
    }
#print(json.dumps(teams,indent=2))

with open("teams.json","w") as make_teams:
    json.dump(teams, make_teams)

