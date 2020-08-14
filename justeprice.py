import random

result = random.randint(0, 100)
choice = 0

while choice != result:
    choice = int(input("choisir un prix:"))

    if choice < result:
        print("c'est plus!")

    elif choice > result:
        print("c'est moins!")
    else:
        print('fin, vous avez gagné!')