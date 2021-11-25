lista = list()

for c in range(0,5):
    num = int(input('Digite um numero: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Numero adicionado ao final da lista....')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos,num)
                print(f'O numero foi inserido na posicao {pos}')
                break
            pos = pos + 1

print(f'A lista ordenada ficou da seguinte forma {lista}')

    
