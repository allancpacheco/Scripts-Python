maior = 0
menor = 0

for c in range(1,6):
    peso = float(input('Digite o peso da pessoa numero {} '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('O maior peso digitado foi {}, e o menor foi {}'.format(maior, menor))