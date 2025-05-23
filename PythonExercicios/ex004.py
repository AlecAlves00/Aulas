#Faça um programa que leia algo pelo teclado e mostre na tela o seu 
# tipo primitivo e todos as informações possiveis sobre ela.
 
n = input('Quantos anos você vai ter em 2050? ')
print('É numeros?',n.isnumeric())
print('É alfabético?',n.isalpha())
print('É apenas letras minúsculo?',n.islower())
print('É apenas maiúsculas?' ,n.isupper())
print (type (n))