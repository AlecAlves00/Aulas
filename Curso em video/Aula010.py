
#Condições * if e else 

nome = str(input('Qual é seu nome?'))
if nome == 'alexander':
    print('Que nome bonito!')
else:
    print('Que nome comum.')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sya média foi ruim! ESTUDE MAIS!')

"""from time import sleep (faz algo demorar os segundos que colocar ex: 
sleep(3) (demore 3 segundos para dar o resultado.) """