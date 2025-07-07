"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,já na posição correta
de inserção (sem usar o sort()).
No final,mostre a lista ordenada na tela.
"""
v = list()
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if c == 0:
        v.append(num)
        print(f'O número {num} foi adicionado no final da lista')
    elif num >= v[-1]:
        v.append(num)
        print(f'O número {num} foi adicionado no final da lista')
    else:
        posicao = 0
        while posicao < len(v):
            if num < v[posicao]:
                v.insert(posicao, num)
                print(f'O número {num} foi adicionado na posição: {posicao}')
                break
            posicao += 1
print(f'A lista ordenada\n{v}')


