n = (
    int(input('Digite um numero de 01 a 10:')),
    int(input('Digite um numero de 01 a 10:')),
    int(input('Digite um numero de 01 a 10:')),
    int(input('Digite um numero de 01 a 10:')),
    int(input('Digite um numero de 01 a 10:'))
    )

print(f'Voce digitou os valores {n}')

print('O numero 9 apareceu {} vezes'.format(n.count(9)))
if 3 in n:
    print ('A orimeira vez que o numero 3 apareceu foi na {} posicao'.format(n.index(3))) #posicao do elemento))
else:
    print('O numero 3 nao foi encontrado')
print ('Os valores pares digitados foram ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')