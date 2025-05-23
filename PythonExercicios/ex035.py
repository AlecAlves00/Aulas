
"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""

primeira = int(input('Digite o comprimento da primeira reta: '))
segunda = int(input('Digite a segunda reta: '))
terceira = int(input('Digite a terceira reta: '))

if primeira + segunda > terceira and primeira + terceira > segunda and segunda + terceira > primeira:
    print('É possível fazer um triângulo com essas medidas.')
else:
    print('Não é possível fazer um triângulo com essa medidas.')