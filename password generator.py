import random
import string

def numberandString(length):
    password=""
    alphabets=string.ascii_letters+string.digits+string.ascii_uppercase
    alphabets=alphabets.replace(" ","").replace("\t","").replace("\n","")
    for i in range(length):
        password=password+random.choice(alphabets)
    if any(character.isdigit() for character in password):
        return (password)
        
    else:
        return numberandString(length)


def onlyString(length):
    password=""
    alphabets=string.ascii_letters+string.ascii_uppercase
    alphabets=alphabets.replace(" ","").replace("\t","").replace("\n","")
    for i in range(length):
        password=password+random.choice(alphabets)
    return (password)


def numberandStringandspec(length):
    
    password=""
    alphabets=string.printable
    alphabets=alphabets.replace(" ","@").replace("\t","@").replace("\n","@")
    for i in range(length):
        password=password+random.choice(alphabets)
    
    if any(char.isdigit() for char in password) and any(not char.isalnum() for char in password):
        return (password)
    else:
        return numberandStringandspec(length)
print("WELCOME TO PASSWORD GENERATOR")
length=int(input("Enter length(4 or more): "))
if length>=4:
    
    print("Complexity:\n")
    print("1. Only characters\n2. Contains at least a number\n3. Contains at least one number and one special character\n")
    select=int(input("Choose complexity: "))
    if select==1:
        pas=onlyString(length)
        print("Password generated: \n",pas)
    elif select==2:
        pas=numberandString(length)
        print("Password generated: \n",pas)
    elif select==3:
        pas=numberandStringandspec(length)
        print("Password generated: \n",pas)
        

    else:
        print("Invalid selection")
else:
    print("Choose length 4 or more.")