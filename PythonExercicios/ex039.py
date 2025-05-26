"""Faça um programa que leia o ano de nascimento de um jovem e informe,de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se já passou do tempo do alistamento.

Seu programa devera mostrar o tempo que falta ou que já passou do prazo.
"""
from datetime  import datetime
ano = int(input('Qual o ano que você nasceu?  '))
idade = datetime.now().year - ano 
if idade < 18:
    print('Você devera se alistar com 18 anos, daqui a {}'.format(18 - idade))
elif idade == 18:
    print('Você devera se alistar esse ano!')
else:
    print('Você deveria se alistar com 18 anos, passou {} anos do tempo.'.format(idade - 18))
    
