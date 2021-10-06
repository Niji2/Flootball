s1, s2, s3 = 100, 100, 100

def RNG():
    global s1, s2, s3
    s1 = (171 * s1) %  30269
    s2 = (171 * s2) %  30307
    s3 = (171 * s3) %  30323
    return (s1/30269 + s2/30307 + s3/30323) % 1.0 

fname1 = "Sylvia"
lname1 = "Letourneau"

#use as (character name) = CharCreate(Character's first name, Character's last name) 
#everything els handled by RNG
def CharCreate(fname, lname):
    i = {
        "First Name": fname,
        "Last Name": lname,
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

Character = CharCreate(fname1, lname1)
print(Character)
