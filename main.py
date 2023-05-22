def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn


import joblib

model = joblib.load('model.joblib')

# pred = model.predict([[0,0.6,1,0.6,1,0,0,0,0,10,10]])
# print(pred)


def askYN(qn):
    inp = input(qn)
    if 'y' in inp:
        return 1
    else:
        return 0

def askInt(qn):
    inp = input(qn)
    return int(inp)

def askFloat(qn):
    inp = input(qn)
    return float(inp)

def calcDigits(string):
    digit = 0
    for ch in string:
        if ch.isdigit():
            digit = digit + 1
        else:
            pass
    return digit

username = input("What is the username?")
fullname = input("What is the fullname?")


pp = askYN("Is there a profile picture? (y/n) :")
numbylenu = calcDigits(username) / len(username)
fullnamewords = len(fullname.split(' '))
numbylenf = calcDigits(fullname) / len(fullname)
nameeqfull = username == fullname
dlength = len(input("Copy paste the description: ").replace(" ",""))
haveURL = askYN("Is there an external link or url in the description? (y/n): ")
isPrivate = askYN("Is that a private account? (y/n): ")
posts = askInt("How many posts have?")
followers = askInt("How many followers have?")
follows = askInt("How many following have?")

pred = model.predict([[pp,numbylenu,fullnamewords,numbylenf,nameeqfull,dlength,haveURL,isPrivate,posts,followers,follows]])
print(pred)

if pred[0] == 1:
    print("The account is fake")
else:
    print("The account is NOT fake")

