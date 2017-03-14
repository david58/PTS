import getpass
import hashlib

def autentifikuj():
    hash_hesla = "61708b0954ee866933b3a2e32340f53033a96c3a680761fd88532a39"
    print("Zadaj heslo!")
    heslo = getpass.getpass(prompt='Password: ', stream=None)
    if(hashlib.sha224(heslo.encode()).hexdigest()==hash_hesla):
        return(True)
    else:
        print("Nesprávne heslo")
        return(False)


autentifikuj()
