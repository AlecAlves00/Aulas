
#Um professor quer sortear a ordem de apresentação de trabalhos dos alunos.Faça um programa que leia
#o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle

n = ['Claudia', 'Luiza', 'Pedro', 'Kaua']
shuffle(n)
print ('A ordem de apresentação sera em primeiro {}, em segundo {}, em terceiro {} e em quarto {}'.format(n[0],n[1],n[2],n[3]))