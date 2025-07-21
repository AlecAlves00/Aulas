"""
Faça um programa que leia nome e média de um aluno,guardando também a situação em um dicionário.No final, mostre o conteúdo 
da estrutura na tela.
"""
aluno = {}
aluno['Nome'] = input('Nome: ')
aluno['Media'] = float(input('Média: '))
print(f'Nome é: {aluno["Nome"]}')
print(f'Média é: {aluno["Media"]}')
if aluno["Media"] >= 7:
        print('Situação é aprovado')
else:
        print('Situação é reprovado')

