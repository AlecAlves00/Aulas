"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
caso esteja errado,peça a digitação novamente até ter um valor correto.
 """

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual é o seu sexo? [M] ou [F] ')).upper().strip()
if sexo == 'M':
        print(f'Você se identifica com o sexo Masculino/{sexo}')
if sexo == 'F':
        print(f'Você se identifica com o sexo Feminino/{sexo}')
#no while poderia usar o 'not in 'MmFf'' ao inves de 'and'