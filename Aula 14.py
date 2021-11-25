'''print('Usando for')

for c in range (1,10):
    print(c)
print('FIM')


print('Usando while')

ct = 1
while ct < 10:
    print(ct)
    ct = ct + 1
print('FIM')

n = 1

while n != 0:
    n = int(input('Digite um valor:'))
print('Parou') 

n = 1
r = 'S'

while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM') '''

n = 1

par = impar = 0

while n != 0:
    n = int(input('Digite um valor:'))
    if(n != 0):
        if n % 2 == 0:
           par = par + 1
        else:
           impar = impar + 1
print('Voce digitou {} numeros pares e {} numeros impares'.format(par,impar)) 



