"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.No final,mostre um boletim contendo a média de cada um 
e permita que o usuário possa mostrar as notas de cada aluno individualmente. 
"""

dados = list()
nome = list()
nota1 = list()
nota2 = list()
resposta = ''
count = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])
    resposta = str(input('Deseja continuar? [S/N]: '))
    if resposta in 'Nn':
        break
print('-='*30)
print('NUM       NOME     Media')
for n,c in enumerate(dados):
    print(f'{n}         {c[0]}      {c[2]}')
while True:
    pessoa = int(input('Mostrar notas de qual aluno?: [Interrompe 999]: '))
    if pessoa != 999:
        print(f'Nota de:{dados[pessoa][0]}, São : {dados[pessoa][1]}')
    else:
        break