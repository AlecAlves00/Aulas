
#Crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada.

n = int(input('Escreva um número: '))
print('O número digitado é {} o dobro do seu numero é {}, o triplo é {} e a raiz quadrada é {:.0f}'.format(n, n*2, n*3, n**(1/2)))