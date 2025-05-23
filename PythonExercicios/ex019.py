
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
#que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice
 
lista = ['lucas', 'bia', 'gabriel', 'jessica']
e = choice(lista)
print('Quem foi escolhido para ajudar foi {}'.format(e))