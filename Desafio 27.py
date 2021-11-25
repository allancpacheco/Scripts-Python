nome = input('Digite seu nome: ')

lista = nome.split()

print(lista)

print('Primeiro nome e: {}'.format(lista[0]))
print('Ultimo nome e: {}'.format(lista[len(lista)-1])) ## Conta a quantidade de casas e diminui uma para ultima posicao
