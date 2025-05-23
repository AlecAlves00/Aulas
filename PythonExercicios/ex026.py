
#Faça um porograma que leia uma frase pelo teclado e mostre:
# 1- Quantas vezes aparece a letra "A"
# 2- Em que posição ela aparece a primeira vez
# 3- Em que posição ela aparece a última vez.

frase = input('Digite uma mensagem: ').upper().strip
f1 = frase.count('A')
print('A quantidade de letras "A" que tem na sua mensagem é: {}'.format(f1))
f2 = frase.find('A')
print('A posição que a primeira letra "A" aparece é: {}' .format(f2 + 1))
f3 = frase.rfind('A')
print('A posição que a última letra "A" aparece é: {}'.format(f3 + 1))



