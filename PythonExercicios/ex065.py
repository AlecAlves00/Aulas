"""Crie um programa que leia vários números inteiros pelo teclado.No final da execução, mostre a média entre todos os valores e qual 
foi o maior e o menor valores lidos. O progarama deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

contador = 0
maior = 0
menor = 0
soma = 0
resp = 'S'

while resp in 'Ss':
    numeros = int(input('Digite um número: '))
    contador += 1
    if contador == 1:
        maior = numeros
        menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
    soma += numeros
    media = float(soma / contador)
    sair = (str(input('DESEJA CONITNUAR?? [S/N]: '))).upper().strip()[0]
print(f'A média dos valores digitados é {media:.1f}, o maior número digitado é {maior} e o menor número digitado é {menor}.')

