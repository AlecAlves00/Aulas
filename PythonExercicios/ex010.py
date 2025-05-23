
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dóçares ela pode comprar.
#Considere US$1,00 = R$3,27.

reias = float(input('Quanto Reais em espécie você tem na sua carteira? : '))
dolares = reias / 3.27
print('com R${:.2f} você tem esse valor em US$ : {:.2f}'.format(reias,dolares))