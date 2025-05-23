print('\033[1;31;43mOlá, Mundo!\033[m')
print('\033[4;30;45mOlá, Mundo!\033[m')
print('\033[7;33;44mOlá, Mundo!\033[m')
print('\033[0;0;0mOlá, Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))
nome = 'Alec'
print('Olá! Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m',nome,'\033[m'))

cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretobranco':'\033[7;30m',
        'verde':'\033[32m',
        'vermelho':'\033[31m'}
print('Olá, Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretobranco'],nome,cores['limpa']))
