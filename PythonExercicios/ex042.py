"""Refaça o desafio 035 dos triângulos,acrescentando o recurso de mostrar que tipo de  triângulo será formado:
-Equilátero:todos os lados iguais
-Isósceles:dois lados iguais 
-Escaleno:todos os lados diferentes !=
"""

r1 = int(input('Digite o primeiro tamanho:  '))
r2 = int(input('Digite o segundo tamanho:  '))
r3 = int(input('Digite o terceiro tamanho:  '))

if  r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 and r1 == r3 and r2 == r3:
            tipo = 'Equilátero'
    elif r1 == r2 or r1 == r3 or r2 == r3:
            tipo = 'Isósceles'  
    elif r1 != r2 and r1 != r3 and r2 != r3:
            tipo = 'Escaleno' 
    print('o tipo de triângulo descrito é {}.'.format(tipo))
else:
       print('Essas retas não podem formar um triângulo.')