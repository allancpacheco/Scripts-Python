lista = []
num = 0

while True:

    num = int(input('Digite um numero: '))
    if num not in lista:
        lista.append(num)
        print('Numero inserido com sucesso')
    else:
        print('O numero ja existe na lista')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar ?? (S/N) ')).strip().upper()[0]
    if opcao == 'N':
           break

lista.sort()
print(f'Os numeros digitados foram {lista}')