print('1.addition \n2.soustraction\n3.division\n4.multiplication')

num1 = int(input("saisir le 1er nombre:"))
num2 = int(input("saisir le 2nd nombre:"))
op = int(input('votre opération:'))

if op == 1:
    result = num1 + num2
    print(result)

elif op == 2:
    result = num1 - num2
    print(result)

elif op == 3:
    result = num1 / num2
    print(result)

elif op == 4:
    result = num1 * num2
    print(result)

print(result)