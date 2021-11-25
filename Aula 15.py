'''cont = 1

while True: # looping infinito #cont <= 10:
    print(cont, '->', end = '')
    cont +=1
print('Acabou') '''

n = s = 0
while True: # while com flag
    n = int(input('Digite um numero: '))
    if n == 999:
        break # Interrompendo o looping
    s += n
print('A soma vale {}'.format(s))
print(f'A soma vale {s}') # Interpolacao de strings