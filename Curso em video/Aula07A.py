
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma entre os numeros é {},\nO produto é {} e a \nDivisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira{} e potência {}'.format(di, e))

#Esse contra barra n "\n" serve para quebrar a linha dentro da função print sem precisar criar outro print.
#Esse ", end=' ' " é  para juntar na mesma linha dois ou mais prints.
#Esse ":.3f", ( o "f" é de float) dentro das chaves {} serve para formatar o numero resultado com apenas 3 casas após a virgula/ponto.
