"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadrastre-os em uma lista.
Caso o número ja exista lá dentro,ele não será adicionado.
No final,serão exibidos todos os valores únicos
digitados,em ordem crescente.
"""
resp = 'S'
valores = list()
while resp in 'Ss':
    c = (int(input('Digite valores: ')))
    if c  not in valores:
        valores.append(c)
        print ('valor foi adiconado com sucesso!')
    else:
        print ('valor não foi adicionado!')
    resp = str(input('Deseja continaur? [S/N]: ')).upper().strip()
valores.sort()
print(f'Os números digitados em ordem crescente é : {valores}')
