nom = input("votre nom :")
print('bienvenue au cinéma de Paris', nom)
 
age = int(input('votre age svp:'))
price = 0

if age < 12:
    price = 7

else:
    price = 10

food = input('voulez vous une confiserie?')

if food == 'yes':
    price += 5
    print('cela vous fera {}$'.format(food))

else:
    print('cela vous fera {}$'.format(price))