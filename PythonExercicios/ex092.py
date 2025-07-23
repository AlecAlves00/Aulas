"""
Crie  um programa que leia nome,ano de nascimento e carteira de trabalho e cadrastre-os (com idade) em um dicionário se por acaso o 
CTPS for diferente de ZERO,o dicionário receberá  também o ano de contratação e o salário. Calcule e acrescente ,além da idade, com 
quantos anos a pessoa vai se aposentar.
"""

from datetime import datetime 

dados = {}

dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['Carteira  de Trabalho'] = int(input('CTPS (0 não tem): '))
dados['Idade'] = datetime.now().year - nascimento 
if dados['Carteira  de Trabalho'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = int(input('Salário: R$ '))
    dados['aposentadoria'] = (dados['Idade'] + 35) - (datetime.now().year - dados['Ano de contratação'])
for k, v in dados.items():
    print(f'{k} tem o valor {v}')