
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex:.Digite um número :1834
#Unidade:4
#Dezena:3
#Centena:8
#Milhar:1

n = str(input('Digite um número de 0 a 9999 : '))
n_separado = n.replace('',' ')
n_formatado = n_separado.strip()
n_lista = n_formatado.split()
print('O número digitado é: {}, sua unidade é: {}, sua dezena é: {}, sua centena é: {} e seu milhar é: {}'.format(n,n_lista[3],n_lista[2],n_lista[1],n_lista[0]))

#Como ele fez - Jeito certo

num = int(input('Digite seu um número de 0 a 9999 : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Seu número é {}, a unidade {}, a dezena é {}, a centena é {} e o milhar é {}'.format(num,u,d,c,m))