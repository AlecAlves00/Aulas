
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite o ano que você deseja descobrir se é bissexto: '))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano é bissexto.')
        else:
            print ('O ano não é bissexto')
    else:
        print('ele é um ano bissexto')
else:
    print('O ano não é bissexto')