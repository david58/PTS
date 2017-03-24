import hashlib
import sys

#REVIEW: chyba dokumentacia cez docstringy

# vyziada a overi heslo
def autentifikuj():
    hash_hesla = open("heslo.txt").read().strip()
    heslo = input("Zadaj heslo!\n")
    # neda sa jednoducho testovat
    # heslo = getpass.getpass(prompt='Heslo: ', stream=None)
    if hashlib.sha224(heslo.encode()).hexdigest() == hash_hesla:
        return True
    else:
        print("Nesprávne heslo")
        return False


def points(hrac, body):
    if autentifikuj():
        if hrac in hraci:
            hraci[hrac]["body"] += body
        else:
            hraci[hrac] = {}
            hraci[hrac]["junior"] = False
            hraci[hrac]["body"] = body
            

def reduction(percenta):
    if autentifikuj():
        for hrac in hraci:
            percent = 1 - percenta / 100
            hraci[hrac]["body"] = int(hraci[hrac]["body"] * percent)
            

def junior(hrac):
    if autentifikuj():
        if hrac in hraci:
            hraci[hrac]["junior"] = True
        else:
            hraci[hrac] = {}
            hraci[hrac]["body"] = 0
            hraci[hrac]["junior"] = True


def ranking(vsetci):
    if vsetci:
        for hrac in sorted(hraci.items(), key=lambda x: x[1]["body"], reverse=True):
            print(hrac[0], hrac[1]["body"])
    else:
        for hrac in sorted(hraci.items(), key=lambda x: x[1]["body"], reverse=True):
            if hrac[1]["junior"]:
                print(hrac[0], hrac[1]["body"])


def myquit():
    if autentifikuj():
        sys.exit()

#REVIEW: hraci tiez nemusia byt globalna premenna, radsej parameter do funkcii
# zoznam hracov
hraci = {}

# REVIEW: program si ma na zaciatku vypytat nove heslo od uzivatela
# ANSWER: ktorá veta v zadaní to hovorí?

if __name__ == "__main__":
    if autentifikuj():
        while True:
            prikaz = input().split()
            # prazdny riadok
            if len(prikaz) == 0:
                continue
            elif prikaz[0] == "points":
                points(prikaz[1], int(prikaz[2]))
            elif prikaz[0] == "reduce":
                reduction(int(prikaz[1]))
            elif prikaz[0] == "junior":
                junior(prikaz[1])
            elif prikaz[0] == "ranking":
                if len(prikaz) > 1 and prikaz[1] == "junior":
                    vsetci = False
                else:
                    vsetci = True
                ranking(vsetci)
            elif prikaz[0] == "quit":
                myquit()
