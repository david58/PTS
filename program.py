import getpass
import hashlib

def autentifikuj():
    hash_hesla = "61708b0954ee866933b3a2e32340f53033a96c3a680761fd88532a39"
    print("Zadaj heslo!")
    heslo = getpass.getpass(prompt='Heslo: ', stream=None)
    if(hashlib.sha224(heslo.encode()).hexdigest()==hash_hesla):
        return(True)
    else:
        print("Nesprávne heslo")
        return(False)


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
        print(prikaz)
        if(prikaz[0] == "points"):
            if(autentifikuj()):
                quit()
        elif(prikaz[0] == "reduce"):
            if(autentifikuj()):
                quit()
        elif(prikaz[0] == "junior"):
            if(autentifikuj()):
                quit()
        elif(prikaz[0] == "ranking"):
            print("done")
        elif(prikaz[0] == "quit"):
            if(autentifikuj()):
                quit()
        
