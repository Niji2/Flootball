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



# Hello people


# time to think about the soccer side of things
# so we got Shoot, Pass, and Dribble to design. 
# along with Punt, Throw in, and Corner kick to do
# also Goal Kick for them penalties.
# so like
# for dribble / passing
# i gotta figure out where they are and make sure they dont pass out of bounds

# x is 1,2,3 = O,M,D
# y is 1,2,3 = L,M,R
# Z is 1,2,3 = MM,OM/DM,G


def SloccerSelect(owner, theif, fspot):
    #check for middle three collums
    if(fspot[2] == "O"):
        BC = owner["DEF"][1]
        Grr = theif["WR"][1]
        x = 1
    elif(fspot[2] == "M"):
        BC = owner["RB"][1]
        Grr = theif["RB"][1]
        x = 2
    else:
        BC = owner["WR"][1]
        Grr = theif["DEF"][1]
        x = 3
    GK = theif["QB"][1]
    #check y cord ( right side left side) of feild
    if(fspot[0] == "M"):
        y = 2
    elif(fspot[0] == "L"):
        y = 1
    else: y = 3
    #check fif in goal distance
    if(x == 1 or x == 3):
        if fspot[1] == "M":
            z = 2
        else: z = 3
    else:
         z = 1 
    return BC, Grr, GK, x, y, z, 

def returntostring(x,y,z,fspot):
    if y == 1:
        fspot[0] = "L"
    elif y == 2:
        fspot[0] = "M"
    else:
        fspot[0] = "R"
    if x == 1:
        fspot[1] = "O"
    if x == 2:
        fspot[1] = "M"
    if x == 3:
        fspot[1] = "D"
    if z == 1 or z == 2:
        fspot[2] = "M"
    if z == 3:
        fspot[2] = "M"
    return fspot
    
def PassBall(teams, owner, theif, score, fspot):
    BC, Grr, GK, x,y,z = SloccerSelect(owner, theif, fspot)
    #the code
    fspot = returntostring(x,y,z,fspot)
    
    
