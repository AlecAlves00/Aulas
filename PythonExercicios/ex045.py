
"""Crie um programa que faça o computador jogar jokenpô com você."""

from random import randint

usuario = int(input("""Vamos jogar jokenpô escoha uma das opcão:
0-Pedra
1-Papel
2-Tesoura
"""))
itens = ['Pedra', 'Papel', 'Tesoura']
maquina = randint(0,2)
if usuario == 0 and maquina == 1:
    final = 'Que pena você perdeu. Tente novamente.'
elif usuario == 0 and maquina == 2:
    final = 'Parabéns você venceu!!!!'
elif usuario == 1 and maquina == 0:
    final = 'Parabéns você venceu!!!!'
elif usuario == 1 and maquina == 2:
    final = 'Que pena você perdeu. Tente novamente.'
elif usuario == 2 and maquina == 0:
    final = 'Que pena você perdeu. Tente novamente.'
elif usuario == 2 and maquina == 1:
    final = 'Parabéns você venceu!!!!'
elif usuario == 0 and maquina == 0 or usuario == 1 and maquina == 1 or usuario == 2 and maquina == 2:
    final = 'Empate. Tente novamente.'
else:
    print('Opcão invalidade, escolha uma das opções corretamente.')
print('O escolhido pela maquina foi {} e por você foi {}, então {}'.format(maquina,usuario,final))
