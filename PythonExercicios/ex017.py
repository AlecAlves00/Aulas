
#Faça um programa que leia o comprimento do cateto adjacente de um triângulo retângulo
#calcule e mostre o comprimento da hipotenusa.

from math import hypot

a = float(input('Qual é o tamanho do cateto oposto?: '))
b = float(input('Qual é o tamanho do cateto adjacente?: '))
c = hypot(a,b)
print('Com o cateto oposto do tamanho de {:.0f} e o tamanho do cateto adjacente de {:.0f},sua hipotenusa é: {:.2f}'.format(a,b,c))