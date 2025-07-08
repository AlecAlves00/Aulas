"""
listas
print(pessoas[0][0]) #Item 0 da lista na posição 0 mostra Pedro
print(pessoas[1][1]) #Mostraria 19 o item 1 da lista 1
print(pessoas[2][0]) #Mostra João, lista na posição 2 e item na posição 0
print(pessoas[1])    #Mostra a lista completa na posição 1 ['Maria', 19]


exercicios:"""

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) # muito importante o '[:]' para criar uma copia e nao fazer uma ligação entre o teste e o galera
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera1 = list()
galera1 = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
for p in galera1:
    print(f'{p[0]} tem {p[1]} anos de idade.')


galera2 = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()
print(galera2)
for p in galera2:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')