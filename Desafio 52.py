n = int(input('Digite um numero: '))

tot = 0

for c in range(1, n + 1):
    if(n % c == 0):
        tot = tot + 1
    else:
        tot = tot

if(tot == 2):
    print('O numero {} E PRIMO'.format(n))
else:
    print('O numero {} NAO E PRIMO'.format(n))