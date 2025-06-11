'''Faça um programa que mostre a tabuada de vários números,um de cada vez,para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

numero = int(input('Digite o valor que deseja fazer a tabuada: '))
contador = 0
while True:
    contador += 1
    resultado = numero * contador
    print(f'{numero} x {contador} = {resultado}')
    if contador == 10:
        numero = int(input('Digite outro número: '))
        contador = 0
    if numero < 0:
        break
print('VOLTE SEMPRE')

