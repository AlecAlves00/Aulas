"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário 
digitar o valor 999,que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando flag).
"""

numero = 0
soma = 0
contador = 0

while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero != 999:
        soma = numero + soma
        contador += 1
print(f'A quantidade de números digitados foi {contador} e a soma dos numeros digitados é → {soma}')
print('FIM!')