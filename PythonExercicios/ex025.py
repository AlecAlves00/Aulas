
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual seu nome completo?: '))
ter = nome.upper().find('SILVA')
if ter<0:
    print('O seu nome {}, não possui "SILVA"'.format(nome))
else:
    print('O seu nome {}, tem "SILVA"'.format(nome))

#Como ele fez - bem mais facil , usando o 'IN'

nome1 = str(input('Qual é seu nome completo')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome1.upper()))