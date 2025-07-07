"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.Seu aplicativo deverá
analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.
"""

expressao = str(input('Digite a expressão: '))
parenteses = list()
for c in expressao:
    if c == '(' :
        parenteses.append(c)
    elif c == ')' :
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(c)
            break
if len(parenteses) == 0:
    print('A expressão está correta!')
else:
    print('A expressão está incorreta!')
    