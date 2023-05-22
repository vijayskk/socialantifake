def warn(*args, **kwargs):
    pass
import warnings
import platform
warnings.warn = warn
import joblib
import os
model = joblib.load('model.joblib')



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

def clearTerminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def printUnderlined(text):
    print(f"\033[4m{text}\033[0m")

def printNewline(n):
    for i in range(n):
        print("\n")


clearTerminal()

printUnderlined("How it works")

printNewline(1)

print("This program will predict a social media account fake or not. All you have to do is give answers for the following questions.\nPlease note that the the model only have 90% accuracy. So don't take it as a final destination.")
printNewline(3)
input("Press enter to continue...")

clearTerminal()

username = input("What is the username? :")
fullname = input("What is the fullname? :")
pp = askYN("Is there a profile picture? (y/n) :")
numbylenu = calcDigits(username) / len(username)
fullnamewords = len(fullname.split(' '))
numbylenf = calcDigits(fullname) / len(fullname)
nameeqfull = username == fullname
dlength = len(input("Copy paste the description: ").replace(" ",""))
haveURL = askYN("Is there an external link or url in the description? (y/n): ")
isPrivate = askYN("Is that a private account? (y/n): ")
posts = askInt("How many posts have? :")
followers = askInt("How many followers have? :")
follows = askInt("How many following have? :")

pred = model.predict([[pp,numbylenu,fullnamewords,numbylenf,nameeqfull,dlength,haveURL,isPrivate,posts,followers,follows]])

printNewline(2)

if pred[0] == 1:
    print("The account is fake")
else:
    print("The account is NOT fake")

printNewline(2)
