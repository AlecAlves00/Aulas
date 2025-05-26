"""
* condições aninhadas

if
elif = pode ter quantos elif quiser dentro do if.
else = só pode ter um else no final do if.
# Exemplo de condições aninhadas"""

nome = str(input('Qual é seu nome? ')).strip().capitalize()
if nome == 'alexander':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Seu nome é bem feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia,{}!'.format(nome))











