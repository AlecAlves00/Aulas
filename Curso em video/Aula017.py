

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

