
"""Desenvolva um prograna qye pergunte a distância de uma viagem em Km.Calcule o preço
da passagem,cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""

distancia = int(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    p = distancia * 0.50
    print('Você deve pagar R${:.2f}!'.format(p))
else:
    s = distancia * 0.45
    print('Você deve pagar R${:.2f}'.format(s))