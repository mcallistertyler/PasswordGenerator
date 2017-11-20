import string
import random
from bs4 import BeautifulSoup
##Generates a strong or weak password
symbols = ['!', '(', ')', '-', '.', '_', '~', '@', '#', '\'', '\"']

def weakGenerate():
  weakWords = ["Copper", "Explain", "Ill", "Truck", "Neat", "Unite", "Branch", "Educated", "Tenous", "Hum", "Decisive", "Notice"]
  return str(random.choice(weakWords))

def randomLowerCase():
  return str(random.choice(string.ascii_lowercase))

def randomUpperCase():
  return str(random.choice(string.ascii_uppercase))
  
def randomNumber():
  return str(random.randint(0,9))

def randomSymbol():
  return str(random.choice(symbols))

functionList = [randomLowerCase, randomUpperCase, randomNumber, randomSymbol]

def passwordGenerator():
  strength = input("How long strong should your password be? (strong/weak)")
  password = ""
  if(strength == "strong"):
    for x in range(0, random.randint(10,15)):
      password += random.choice(functionList)()
    if(any(x.isupper() for x in password) == False):
      password += randomUpperCase()
    if(any(x.islower() for x in password) == False):
      password += randomLowerCase()
    if(any(x in password for x in symbols) == False):
      password += randomSymbol()
    if(any(x.isdigit() for x in password) == False):
      password += randomNumber()
    return password
    
  elif(strength == "weak"):
    password += weakGenerate() + randomNumber() + randomNumber() + randomNumber() + randomSymbol()
    return password
    
      
    
def main():
  print(passwordGenerator())

main()