
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,com 5% de desconto.

C = input('Bem-vindo o que você deseja comprar aqui na loja? ')
cores = {'limpa':'\033[m',
        'verde':'\033[32m',
        'vermelho':'\033[31m'}
        
preco = 3245
desc = preco * 0.05
final = preco - desc
print('O preço do seu produto era:{}{}{} e com o desconto de:{}{}{} foi para:{}{}{}'.format(cores['vermelho'],preco,cores['limpa'],cores['verde'],desc,cores['limpa'],cores['verde'],final,cores['limpa']))
