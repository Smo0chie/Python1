#Korrutamine10nepiires
print("Mis su nimi on?")
myName=input()
print("Tere " + myName)
from random import *
a = (randint(1, 10))
b = (randint(1, 10))
c= input("Palju on " + str(a) + "*"+ str(b) + "?")
if int(c) == (a * b):
    print("Õige")
else:
    print("Vale")
d= input("Kas arvutame veel?")
while d == "ja":
    a = (randint(1, 10))
    b = (randint(1, 10))
    c= input("Palju on " + str(a) + "*"+ str(b) + "?")
    d = input("Kas arvutame veel ?")
else:
    print("Headaega!")

    
   
    

    

    
