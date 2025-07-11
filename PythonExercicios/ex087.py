"""
Aprimore o desafio anterior, mostrando no final :
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

listageral = [[],[],[]]
somapares = 0

for linha in range(3):
    for coluna in range(3):
        num = int(input(f'Digite um valor para [{linha} , {coluna}] : '))
        listageral[linha].append(num)
        if num % 2 == 0:
            somapares += num
for linha in listageral:
    for valor in linha:
        print(f'[ {valor:^3} ]', end = '')
    print()
somacoluna = listageral[0][2] + listageral[1][2] + listageral[2][2]
print(f'A soma de todos os valores pares digitados são: {somapares}')
print(f'A soma dos valores da terceira coluna é: {somacoluna}')
print(f'O maior valor da segunda linha é: {max(listageral[1])}')