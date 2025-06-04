"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,desconsideranddo os espaços."""

frase = str(input('Qual a frase que deseja descobrir se é um palíndromo:  '))
frase = frase.upper()
pali = frase[::-1]
pali = pali.upper()
if frase == pali:
    print(f'A frase digitada é um palíndromo {frase},{pali}')
else:
    print('Essa frase não é um palíndromo.')

frase1 = str(input('Digite um frase:  ')).strip().upper()
palavras = frase1.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palídromo!')