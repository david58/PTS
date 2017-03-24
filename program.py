import hashlib


# vyziada a overi heslo
def autentifikuj():
    hash_hesla = open("heslo.txt").read().strip()
    heslo = input("Zadaj heslo!\n")
    # neda sa jednoducho testovat
    # heslo = getpass.getpass(prompt='Heslo: ', stream=None)
    #REVIEW: if nepotrebuje zatvorky a je to neidiomaticke
    if(hashlib.sha224(heslo.encode()).hexdigest() == hash_hesla):
        return True
    else:
        print("Nesprávne heslo")
        return False


def points():
    #REVIEW: globalna premenna prikaz, vid ranking
    #REVIEW: if nepotrebuje zatvorky a je to zle
    if(autentifikuj()):
        if prikaz[1] in hraci:
            hraci[prikaz[1]]["body"] += int(prikaz[2])
        else:
            hraci[prikaz[1]] = {}
            hraci[prikaz[1]]["junior"] = False
            hraci[prikaz[1]]["body"] = int(prikaz[2])
            

def reduction():
    #REVIEW: globalna premenna prikaz, vid ranking
    if(autentifikuj()):
        for hrac in hraci:
            percent = 1 - int(prikaz[1]) / 100
            hraci[hrac]["body"] = int(hraci[hrac]["body"] * percent)
            

def junior():
    #REVIEW: globalna premenna prikaz, vid ranking
    if(autentifikuj()):
        if prikaz[1] in hraci:
            hraci[prikaz[1]]["junior"] = True
        else:
            hraci[prikaz[1]] = {}
            hraci[prikaz[1]]["body"] = 0
            hraci[prikaz[1]]["junior"] = True


def ranking():
    #REVIEW: tu sa dana podiferne vytvorena globalna premenna pouziva
    #        bez spustenia som myslel, ze to crashne
    #        tato funkcia nie je pouzitelna, pokial sa dopredu nenastavi globalna
    #        premenna prikaz, velmi zle
    #        premennu prikaz nie je dobre dat ani ako parameter priamo
    #        spravny sposob je sparsovat ju v hlavnom cykle a potom dat funkcii ranking
    #        napriklad boolovsky parameter junior
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

#REVIEW: nejaky kod by sa mal v pythone spustat len ak plati
#        if __name__ == "__main__":
#        cize ak tento subor neimportujeme ale spustame
if(autentifikuj()):
    #REVIEW: while nepotrebuje zatvorky a je to zle
    while(True):
        #REVIEW: velmi pofiderne vytvorena globalna premenna
        #        vobec nie je na prvy pohlad jasne, preco toto funguje
        prikaz = input().split()
        # prazdny riadok
        #REVIEW: if nepotrebuje zatvorky a je to neidiomaticke
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
