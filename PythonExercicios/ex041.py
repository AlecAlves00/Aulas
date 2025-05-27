"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos : MIRIM
-Até 14 anos : INFANTIL
-Até 19 anos : Junior
-Até 20 anos : Sênior
-Acima: Master
"""

idade = int(input('Em que ano você nasceu?:  '))
catego = 2025 - idade
if catego <= 9:
    print('Sua categoria é mirim.')
elif catego >= 14 and catego <=18:
    print('Sua categoria é infantil')
elif catego == 19:
    print('Sua categoria é junior')
elif catego == 20:
    print('Sua categoria é sênior')
else:
    print('Sua categoria é master')