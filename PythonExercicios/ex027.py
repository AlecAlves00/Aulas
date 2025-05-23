#Faça um programa que leia o nome completo de uma pessoa,mostrando em seguida
#o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
n1 = nome.split()
print('Seu primeiro nome é: {}, e seu último nome é: {}'.format(n1[0], n1[-1]))