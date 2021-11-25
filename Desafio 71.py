print('-='*50)
print('BEM VINDO AO SEU BANCO')
print('-='*50)
valor = int(input('Digite o valor que voce quer sacar: R$'))
print('-='*50)
total = valor
ced = 50
qt_cedula = 0

while True:
    if total >= ced:
        total = total - ced
        qt_cedula = qt_cedula + 1
    else:
        if qt_cedula > 0:
            print('Total de {} cedulas de R$ {}'.format(qt_cedula, ced))
        if ced == 50:
           ced = 20
        elif ced == 20:
           ced = 10
        elif ced == 10:
           ced = 1
        qt_cedula = 0
        if total == 0:
            break
print('-='*50)
print('VOLTE SEMPRE AO SEU BANCO')
print('-='*50)