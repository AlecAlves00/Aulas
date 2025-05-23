'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''

num1 = int(input('Digite três números, o primeiro é: '))
num2 = int(input('O segundo número é: '))
num3 = int(input('O terceiro número é: '))
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print('Os números digitados do menor para o maior é:{},{},{}'.format(num3,num2,num1))
    else:
        print('Os números digitados do menor para o maior é:{},{},{}'.format(num2,num3,num1))
else:
    if num1 <= num2 and num1 <= num3:
        if num2 <= num3:
            print('Os números digitados do menor para o maior é:{},{},{}'.format(num1,num2,num3))
        else:
            print('Os números digitados do menor para o maior é:{},{},{}'.format(num1,num3,num2))
    else:
        if num3 <= num2:
            print('Os números digitados do menor para o maior é: {},{},{}'.format(num3,num1,num2))
        else:
            print('Os números digitados do menor para o maior é:{},{},{}'.format(num2,num1,num3 ))
    