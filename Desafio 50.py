s = 0

for c in range(1,7):
    n = int(input('Digite um numero: '))
    if(n % 2 == 0):
         s = s + n
print('A soma dos numeros pares e de: {}'.format(s))