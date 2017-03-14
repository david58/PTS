import getpass
import hashlib

def autentifikuj():
    hash_hesla = "61708b0954ee866933b3a2e32340f53033a96c3a680761fd88532a39"
    print("Zadaj heslo!")
    heslo = input()
    #heslo = getpass.getpass(prompt='Heslo: ', stream=None)
    if(hashlib.sha224(heslo.encode()).hexdigest()==hash_hesla):
        return(True)
    else:
        print("Nesprávne heslo")
        return(False)


hraci={}

if(autentifikuj()):
    print("Zoznam príkazov:\n\n"\
        
    "points <name> <number>\n"\
    "  Pridá hráčovi <name> <number> bodov. Číslo môže byť aj záporné.\n"\
    "  Ak hráč <name> ešte nie je evidovaný, pridá ho do zoznamu s <number> "\
    "bodmi.\n"\
    "  Vyžaduje heslo!\n\n"\
    
    "reduce <number>\n"\
    "  Zníži počet bodov každého hráča o <number> percent. Výsledok sa "\
    "zaokrúhli na celé čísla nadol.\n"\
    "  Vyžaduje heslo!\n\n"\
    
    "junior <name>\n"\
    "  Označí, že hráč <name> je junior\n"\
    "  Vyžaduje heslo!\n\n"\
    
    "ranking\n"\
    "  Vypíše celé poradie. Hráčov zoradí podľa počtu bodov.\n\n"\
    
    "ranking junior\n"\
    "  Vypíše poradie medzi juniormi.\n\n"\
    
    "quit\n"\
    "  Ukončí program.\n"\
    "  Vyžaduje heslo!")
    while(True):
        prikaz = input().split()
        if(prikaz[0] == "points"):
            if(autentifikuj()):
                if prikaz[1] in hraci:
                    hraci[prikaz[1]]["body"] += int(prikaz[2])
                else:
                    hraci[prikaz[1]]={}
                    hraci[prikaz[1]]["junior"] = False
                    hraci[prikaz[1]]["body"] = int(prikaz[2])
        elif(prikaz[0] == "reduce"):
            if(autentifikuj()):
                for hrac in hraci:
                    percent = 1-int(prikaz[1])/100
                    hraci[hrac]["body"] = int(hraci[hrac]["body"]*percent)
        elif(prikaz[0] == "junior"):
            if(autentifikuj()):
                if prikaz[1] in hraci:
                    hraci[prikaz[1]]["junior"] = True
                else:
                    hraci[prikaz[1]]={}
                    hraci[prikaz[1]]["body"] = 0
                    hraci[prikaz[1]]["junior"] = True
        elif(prikaz[0] == "ranking"):
            if(len(prikaz)>1 and prikaz[1]=="junior"):
                for hrac in sorted(hraci.items(), 
                                   key=lambda x: x[1]["body"], 
                                   reverse = True):
                    if(hrac[1]["junior"]):
                        print(hrac[0],hrac[1]["body"])
            else:
                for hrac in sorted(hraci.items(), 
                                   key=lambda x: x[1]["body"], 
                                   reverse = True):
                    print(hrac[0],hrac[1]["body"])
        elif(prikaz[0] == "quit"):
            if(autentifikuj()):
                quit()
        
