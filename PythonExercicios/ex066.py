'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).
'''
contador = 0
soma = 0
while True:
    num = int(input('Digite um número: '))
    if num != 999:
        contador += 1
        soma += num
    else:
        break
print(f'a quantidade de números digitados foi {contador} e a soma entres esses números foi {soma}')


