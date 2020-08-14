import random

print("1.pile\n2.face")

choice = int(input("votre choix?"))

if choice == 1 :
    iachoice = 2

else:
    iachoice = 1

result = random.randint(1 , 2)
print(result)