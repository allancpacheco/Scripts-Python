lista = []
maior = menor = soma = posicao_maior = posicao_menor = 0

for c in range(0,5):
    lista.append(int(input(f'Digite um numero para a posicao {c}: '))) ## incluindo os valores na lista
    if c == 0:
        maior = menor = lista[c]
    if lista[c] > maior:
        maior = lista[c]
    if lista[c] < menor:
        menor = lista[c]

print(f'O maior numero foi {maior} nas posicoes:' , end=' ')

for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end=' ')
print()

print(f'O menor numero foi {menor} nas posicoes:' , end=' ')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end=' ')
print()

