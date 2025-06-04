
frase = 'Curso em Vídeo Python'
print(frase[3:])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase[::-1])

print(frase.count('o'))
print(frase.upper().count('O'))
#transformando tudo em maiscúlo por conta do upper, e contando quantos 'O' tem por conta do count.
print(len(frase))
#para descobrir quantas caracteres tem

print(frase.replace('Python', 'Android'))
#usado para trocar uma str porem deve ser salvo a alterção

print('curso' in frase)
#apenas vai procurar a palavra desejada e se tiver vai dar true ou false.
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
divido = frase.split()
print (divido)
print(divido[0])
print(divido[2][3])
#vai ser divido em lista e pegar a '2' letra ou palavra e dentro da frase ou texto e vai pegar o número '3'
#e mostrar na tela ex: '2' = video , '3' = e .




p = """Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!"""
print(len (p))
#usando ("""texto""") é possivel selecionar todo de uma vez só.