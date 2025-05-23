
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a qunatidade de dias pelos quais ele foi alugado.calcule o preço a pagar,sabendo que
# o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km você percorreu?: '))
dias = float(input('Quantos dias você esta com o carro?: '))
v1 = km * 0.15
v2 = dias * 60
v3 = v1 + v2
print ('Com {:.0f} dias e {:.1f}Km rodados você deve pagar R${:.2f}'.format(dias,km,v3))