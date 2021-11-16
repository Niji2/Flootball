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
        "Flappability": RNG(),
        "Aprosexability": RNG(),
        "Dordbility": RNG(),
        "Imprigrious": RNG(),
        "Macilient": RNG(),
        "Miclewritter": RNG(),
        "Nittiness": RNG(),
        "Noceny": RNG(),
        "Pilliverish": RNG(),
        "Pyknic": RNG(),
        "Scibility": RNG(),
        "Testudineous": RNG(),
        "Yemeles": RNG(),
        "Zoilist": RNG(),
        "Hypersaliant": RNG(),
        "Overwashed": RNG(),
        "Segmented": RNG()
    }
    return i
 
Character = CharCreate()

def TeamCreate():
    i2={"QB": {1:CharCreate()},
        "WR":{1:CharCreate(), 2:CharCreate(), 3:CharCreate()},
        "RB/TE":{1:CharCreate(), 2:CharCreate(), 3:CharCreate(), 4:CharCreate(), 5:CharCreate(), 6:CharCreate()},
        "LB/Safety":{1:CharCreate(), 2:CharCreate(), 3:CharCreate(), 4:CharCreate(), 5:CharCreate(), 6:CharCreate(), 7:CharCreate(), 8:CharCreate(), 9:CharCreate()}}
    return i2
teams = {
        "Orono Juicers": TeamCreate(),
        "Blue Badgers": TeamCreate()
    }
#print(json.dumps(teams,indent=2))

with open("teams.json","w") as make_teams:
    json.dump(teams, make_teams)