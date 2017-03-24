import hashlib
import sys


def autentifikuj():
    """vyziada a overi heslo"""
    hash_hesla = open("heslo.txt").read().strip()
    heslo = input("Zadaj heslo!\n")
    # neda sa jednoducho testovat
    # heslo = getpass.getpass(prompt='Heslo: ', stream=None)
    if hashlib.sha224(heslo.encode()).hexdigest() == hash_hesla:
        return True
    else:
        print("Nesprávne heslo")
        return False


def points(hraci, hrac, body):
    """prida hracovi body"""
    if autentifikuj():
        if hrac in hraci:
            hraci[hrac]["body"] += body
        else:
            hraci[hrac] = {}
            hraci[hrac]["junior"] = False
            hraci[hrac]["body"] = body


def reduction(hraci, percenta):
    """každému zníži počet bodov o percentá"""
    if autentifikuj():
        for hrac in hraci:
            percent = 1 - percenta / 100
            hraci[hrac]["body"] = int(hraci[hrac]["body"] * percent)


def junior(hraci, hrac):
    """označí hráča za juniora"""
    if autentifikuj():
        if hrac in hraci:
            hraci[hrac]["junior"] = True
        else:
            hraci[hrac] = {}
            hraci[hrac]["body"] = 0
            hraci[hrac]["junior"] = True


def ranking(hraci, vsetci):
    """vypíše poradie hráčov"""
    if vsetci:
        for hrac in sorted(hraci.items(), key=lambda x: x[1]["body"], reverse=True):
            print(hrac[0], hrac[1]["body"])
    else:
        for hrac in sorted(hraci.items(), key=lambda x: x[1]["body"], reverse=True):
            if hrac[1]["junior"]:
                print(hrac[0], hrac[1]["body"])


def myquit():
    """ukončí program"""
    if autentifikuj():
        sys.exit()


if __name__ == "__main__":
    hraci = {}
    if autentifikuj():
        while True:
            prikaz = input().split()
            # prazdny riadok
            if len(prikaz) == 0:
                continue
            elif prikaz[0] == "points":
                points(hraci, prikaz[1], int(prikaz[2]))
            elif prikaz[0] == "reduce":
                reduction(hraci, int(prikaz[1]))
            elif prikaz[0] == "junior":
                junior(hraci, prikaz[1])
            elif prikaz[0] == "ranking":
                if len(prikaz) > 1 and prikaz[1] == "junior":
                    vsetci = False
                else:
                    vsetci = True
                ranking(hraci, vsetci)
            elif prikaz[0] == "quit":
                myquit()
