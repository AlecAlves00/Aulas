"""Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho.
#Quantas mulheres têm menos de 20 anos.
"""

media = 0
idadesoma = 0
maior = 0
homem_mais_velho = ''
mulhermenor = 0
for c in range(1,5):
    print('Digite as informações de 4 pessoas')
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))
    idadesoma = idade + idadesoma
    media = float(idadesoma / c)
    sexo = int(input('Digite o sexo dessa pessoa 1 para Masculino e 2 para Feminino: '))
    if sexo == 1 and idade > maior:
       maior = idade
       homem_mais_velho = nome
    elif sexo == 2 and idade < 20:
        mulhermenor += 1
print(f'A média de idade do grupo é {media}\n O nome do homem mais velho é {homem_mais_velho}\n A quantidade de mulher com menos de 20 anos é {mulhermenor} mulher/mulheres.')



