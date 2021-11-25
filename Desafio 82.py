lista = list()
lista_par = list()
lista_impar = list()

while True:
    lista.append(int(input('Digite um numero: ')))
    opcao = input('Quer continuar ? (S/N): ').strip().upper()
    if opcao in 'Nn':
        break

for i,v in enumerate(lista):
   if v % 2 == 0:
       lista_par.append(v)
   else:
       lista_impar.append(v)

print(f'A lista original ficou: {lista}')
print(f'A lista de numeros pares ficou: {lista_par}')
print(f'A lista de numeros impares ficou: {lista_impar}')