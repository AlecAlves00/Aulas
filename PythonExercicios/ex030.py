
#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número para descobrir se é ímpar ou par: '))
if n % 2 == 0:
    print('O número {:.0f} é um número par!'.format(n))
else:
    print('O número {:.0f} é um número ímpar!'.format(n))
