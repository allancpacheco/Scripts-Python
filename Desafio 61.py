p = int(input('Digite o primeiro elemento da PA: '))
r = int(input('Digite a razao da PA: '))
q = int(input('Digite a quantidade de numeros: '))

termo = p
cont = 1

while cont <= q:
    print(termo, end = ' - ')
    termo = termo + r
    cont = cont + 1
print('Fim')
    