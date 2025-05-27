"""Desenvolva uma lógica que leia  o peso e a altura de uma pessoa,calcule sua IMC(INDICE DE MASSA CORPOREA) e mostre seu status, de acordo com
a tabela abaixo:
-Abaixo de 18.5: Abaixo do peso
-Entre 18.5 e 25:Peso ideal
-25 até 30: Sobrepeso
-30 até 40:Obesidade
-Acima de 40:Obesidade mórbida. 
"""

altura = float(input('Digite sua altura:  '))
peso = int(input('Digite seu peso:  '))
imc = peso / (altura * altura) 
if imc <= 18.4:
    esta = 'Abaixo do peso'
elif imc >= 18.5 and imc <= 24:
    esta = 'Peso ideal'
elif imc >=25 and imc <= 29:
    esta = 'Sobrepeso'
elif imc >=30 and imc <=39:
    esta = 'Obesidade'
else:
    esta = 'Obesidade mórbida'
print('Com as informações dadas de  altura de {} e peso de {} kg o seu imc é {2:.f} você esta {}.'.format(altura,peso,imc,esta))