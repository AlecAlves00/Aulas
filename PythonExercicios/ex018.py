
#Faça um programa que leia um ângulo qualquer e msotre na tela o valor do seno,cosseno e tangente desse ângulo.

from math import sin,cos,tan,radians

angulo = float(input('Qual é o ângulo que você deseja? : '))
rad = radians(angulo)
seno = sin(rad)
cosse = cos(rad)
tang = tan(rad)
print ('Seu seno é {:.3f} o cosseno é {:.3f} e a tangente é {:.3f}'.format(seno,cosse,tang))