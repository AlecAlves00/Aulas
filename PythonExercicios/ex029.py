
""" Escreva um programa que leia a velocidade de um carro.
Se ele ultarapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite. """

veloci = int(input('Qual era a velocidade que você estava? : '))
if veloci <= 80:
    print('Você estava na velocidade permitida!')
else:
    nao = (veloci - 80) * 7
    print('Você não estava na velocidade permitida. A multa é de R${:.2f}.'.format(nao))


"""
Velocidade = float(input('Qual é velocidade atual do carro?'))
if velocidade >80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2F}!'.format(multa))
    print('Você esta na velocidade permitida.)
 """