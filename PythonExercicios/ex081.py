"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso,mostre:
A)Quantos números foram digitados.
B)A lista de valores,ordenado de forma decrescente.
C)Se o valor 5 foi digitado e está ou não na lista.
"""
valores = list()
resp = ''
posição = 0
while True:
    num = int(input('Digite um valor: '))
    resp = str(input('Deseja continuar? [S/N]: '))
    valores.append(num)
    if resp in 'Nn':
        break
quantidade = len(valores)
print(f'A quantidade de números digitados é : {quantidade}')
valores.sort(reverse=True)
print(valores)
if 5 in valores:   
   print(f'Essa lista possui o número 5 e esta na posição {valores.index(5)}')
else:
    print('O número 5 não foi digitado nessa lista!')


