"""Melhore o desafio 061,perguntando para o usuário se ele quer mostrar mais alguns termos. O programa 
encerra quando ele disser que quer mostrar 0 termos."""

razao = int(input('Digite a razão: '))
num =  int(input('Digite o número: '))
termo = int(input('Deseja colocar mais termos: '))

while termo != 0:
    contador = 1
    while contador < termo:
        pa = num + contador * razao
        contador += 1
        print(pa)
    termo = int(input('Deseja colocar mais termos: '))