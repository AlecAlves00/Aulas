"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso,crie duas listas externas que vão conter apenas os valores pares e os valores impares digitados,respectivamente.
Ao final,mostre o conteúdo das três listas geradas.
"""
valores = list()
impar = list()
par =  list()
while True:
    num = int(input('Digite os números que deseja [-1 para sair do programa!]: '))
    if num == -1:
        break
    else:
        valores.append(num)
        if num % 2 == 0:
            par.append(num)
            par.sort()
        else:
            impar.append(num)
            impar.sort()
    valores.sort()
print(f'As listas geradas são:\n{valores}\n{impar}\n{par}')