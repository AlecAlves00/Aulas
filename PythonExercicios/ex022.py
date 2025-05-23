
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas.
#O nome com todas as letras minúsculas.
#Quantas letras ao todo(sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ','')))
pnome = nome.split()
print(len(pnome[0]))

#Como ele fez :

nome1 = str(input('Digite seu nome completo: ')).strip()
#strip para retirar os espaços do começo e do fim
print('Seu nome em maiúsculas é {}'.format(nome1.upper()))
print('Seu nome em minúsculas é {}'.format(nome1.lower()))
print('Seu nome tem ao todo {} letras'.foramat(len(nome1) - nome1.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome1.find(' ')))


