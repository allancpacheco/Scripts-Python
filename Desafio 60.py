'''from math import factorial
n = int(input('Digite um numero e descubra seu fatorial : '))
f = factorial(n)
print('O fatorial de {} e {}'.format(n,f))'''


n = int(input('Digite um numero e descubra seu fatorial : '))
c = n
f = 1
print('Calculando fatorial de {}!'.format(n))
while c > 0:
    print('{}'.format(c))
    print(' x ' if c > 1 else ' = ')
    f = f * c
    c = c - 1
print('{}'.format(f))