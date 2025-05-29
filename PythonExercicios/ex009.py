
# Faça um programa que leia  um número inteiro qualquer e mostre na tela a sua tabuada inteira.

p = int(input('Digite um número: '))
print ('Sua tabuada : \n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(p*1,p*2,p*3,p*4,p*5,p*6,p*7,p*8,p*9,p*10)) 

num = int(input('Digite um número: '))
um = str(num) + 'x1 = ' + str(num * 1)
dois = str(num) + 'x2 = ' + str(num * 2)
tres = str(num) + 'x3 = ' + str(num * 3)
quatro = str(num) + 'x4 = ' + str(num * 4)
cinco = str(num) + 'x5 = ' + str(num * 5)
seis = str(num) + 'x6 = ' + str(num * 6)
sete = str(num) + 'x7 = ' + str(num * 7)
oito = str(num) + 'x8 = ' + str(num * 8)
nove = str(num) + 'x9 = ' + str (num * 9)
dez = str(num) + 'x10 = ' + str(num * 10)

print('Sua tabuada é: {} \n{} \n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(num,um,dois,tres,quatro,cinco,seis,sete,oito,nove,dez))