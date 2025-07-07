

#lanche.append('1')'# para adicionar um item na lista
#lanche.insert(0,'cachorro quente') para inserir um elemento onde quiser na lista e modificar as posiçoes dos proximos
#del lanche[3] para apagar o "lanche"
#lanche.pop(3) para eleminar onde voce quiser
#valores.sort() para organizar as coisas ex : 9 0 7 3 2 0 = 0 0 2 3 7 9
#valores.sort(reverse=True) para fazer a ordem de tras para a frente ex: 9 8 7 6 5 4 3 2 1

num = [2, 5, 9, 1]
num[2] = 3
num[4] = 7
num.append(7)
num.sort()
num.insert(2, 0) #colocar elemento na posiçao 2
num.sort(reverse=True)
print(num)

#num.pop() remove o objeto da lista "se nao expecificar remove o ultimo"
#num.append() ele adicona um valor ao final da lista ex: 4,5,6 .append(2) = 4,5,4,6,

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista.')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista.')

a = [2, 3, 4, 7]
b = a[:] 
#cuidado para nao criar um vinculo com duas ramificações de lista sem o [:](que faz o 'b' receber todos os itens do 'a'
#sem isso mudar o b muda também o a )
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')