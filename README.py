# TestToday

#Numero aleatorio
import random
x = random.randint(12,18)
print(x)
if x == 15:
    print("Es 15!!")
else:
    print("Otro número")

#Lista de nombres
Lista= ("Jon","Maria","Juan","Asier")
y= random.choice(Lista)
print(y)
if y == ("Maria") or ("Juan"):
    print("Maria y juan no estan hoy en clase")
elif y == ("Asier") or ("Jon"):
    print("Asier y jon estan en clase")
