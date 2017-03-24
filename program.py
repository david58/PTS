import hashlib


# vyziada a overi heslo
def autentifikuj():
    hash_hesla = open("heslo.txt").read().strip()
    heslo = input("Zadaj heslo!\n")
    # neda sa jednoducho testovat
    # heslo = getpass.getpass(prompt='Heslo: ', stream=None)
    if(hashlib.sha224(heslo.encode()).hexdigest() == hash_hesla):
        return True
    else:
        print("Nesprávne heslo")
        return False


def points():
    if(autentifikuj()):
        if prikaz[1] in hraci:
            hraci[prikaz[1]]["body"] += int(prikaz[2])
        else:
            hraci[prikaz[1]] = {}
            hraci[prikaz[1]]["junior"] = False
            hraci[prikaz[1]]["body"] = int(prikaz[2])
            

def reduction():
    if(autentifikuj()):
        for hrac in hraci:
            percent = 1 - int(prikaz[1]) / 100
            hraci[hrac]["body"] = int(hraci[hrac]["body"] * percent)
            

def junior():
    if(autentifikuj()):
        if prikaz[1] in hraci:
            hraci[prikaz[1]]["junior"] = True
        else:
            hraci[prikaz[1]] = {}
            hraci[prikaz[1]]["body"] = 0
            hraci[prikaz[1]]["junior"] = True


def ranking():
    if(len(prikaz) > 1 and prikaz[1] == "junior"):
        for hrac in sorted(hraci.items(),
                           key=lambda x: x[1]["body"],
                           reverse=True):
            if(hrac[1]["junior"]):
                print(hrac[0], hrac[1]["body"])
    else:
        for hrac in sorted(hraci.items(),
                           key=lambda x: x[1]["body"],
                           reverse=True):
            print(hrac[0], hrac[1]["body"])
            

def myquit():
    if(autentifikuj()):
        quit()
# zoznam hracov
hraci = {}

# REVIEW: program si ma na zaciatku vypytat nove heslo od uzivatela
# ANSWER: ktorá veta v zadaní to hovorí?
if(autentifikuj()):
    while(True):
        prikaz = input().split()
        # REVIEW: skarede a neprehladne, rozdelit do viacerych funkcii
        # prazdny riadok
        if(len(prikaz) == 0):
            continue
        elif(prikaz[0] == "points"):
            points()
        elif(prikaz[0] == "reduce"):
            reduction()
        elif(prikaz[0] == "junior"):
            junior()
        elif(prikaz[0] == "ranking"):
            ranking()
        elif(prikaz[0] == "quit"):
            myquit()
