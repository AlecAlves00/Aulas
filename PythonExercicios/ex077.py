"""
Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
Depois disso,você deve mostrar, para cada palavra,quais são as suas vogais.
"""

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in palavras:
    vogais = ''
    for letra in c:
        if letra in 'aeiou':
            vogais += letra + ' '
    print(f'A palavra {c.upper()} tem essas vogais {vogais.upper()}')
        


    