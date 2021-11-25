lista  = []
opcao = 'S'

while opcao == 'S':
    num = int(input('Digite um numero: '))
    lista.append(num)
    opcao = input('Quer continuar ? (S/N): ').strip().upper()

lista.sort(reverse=True)
print(lista)

if 5 in lista:
    print('O numero 5 faz parte da lista')