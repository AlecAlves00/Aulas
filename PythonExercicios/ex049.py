"""Refaça o desafio 009,mostrando a tabuada de um número que o úsuario escolher,só que agora utilizando um laço for"""

num = int(input('Digite o número que deseja fazer a tabuada:  '))
multi = 0

for c in range(1,11):
    multi = c * num
    print(f"{num}x{c}={multi}")