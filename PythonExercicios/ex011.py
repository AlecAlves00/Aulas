
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua   área e  
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Quanto de largura tem a parede que você gostaria de pintar? : '))
altura = float(input('Quanto de altura a mesma parede tem? : '))
metros = largura * altura 
litros =  metros / 2
print('A quantidade necessária de litros para pintar a sua parede é de :{}' .format(litros))