"""
Crie um programa onde o usuário possa digitar sete valores numeéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente.
"""

principal = list()
par = list() 
impar = list()
for c in range(1,8):
    num = int(input(f'Digete o número {c}º: ' ))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
impar.sort()
principal.append(impar[:])
par.sort()
principal.append(par[:])
print(f'Todos valores digitados foi: {principal} ')
print(f'Os valores pares digitados foi: {par}')
print(f'Os valores impares digitados foi: {impar}')

