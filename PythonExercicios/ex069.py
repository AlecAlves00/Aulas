"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
"""

contadorgeral = 0
mulher_menores = 0
contador_homem = 0

while True:
    idade = int(input('Qual idade: '))    
    sexo = str(input('Qual sexo? [F/M]: ')).upper().strip()[0]
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if idade >= 18:
        contadorgeral += 1
    if sexo in 'Ff' and idade < 20:
        mulher_menores += 1
    if sexo in 'Mm':
        contador_homem += 1
    if continuar in 'Nn':
        break

print('-=-' *30)
print(f'A quantidade de pessoas com mais de 18 anos é {contadorgeral}\nA quantidade de homens cadrastrados é {contador_homem}\nA quantidade de mulheres com menos de 20 anos é {mulher_menores}.')
print('-=-' *30)