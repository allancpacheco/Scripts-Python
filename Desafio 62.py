p = int(input('Digite o primeiro elemento da PA: '))
r = int(input('Digite a razao da PA: '))
## q = int(input('Digite a quantidade de numeros: '))

termo = p
cont = 1
total = 0
mais  = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end = ' - ')
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('Fim')
print ('Progressao finalizada com {} termos'.format(total))
    