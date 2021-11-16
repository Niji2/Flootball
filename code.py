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
# ALSO WHAT THE FUCK VC
# anyway back to celebrating 

i = 0
while i < 37:
    RNG()
    i = i + 1

# wait, new war 2?
# the new war, thats been new for 5 years now?
# the new war, that is no longer fucking new?!?!?!?!?
# WAIT ALL PRIME STUFF IS OUT AGAIN? WHAT THE FUCK?

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
            bar3 = DEF[f] + DEF[g] - (WR[h]/2)
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

    

    

    
    return yards

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