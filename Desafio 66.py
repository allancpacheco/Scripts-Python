n = s = c = 0
while True: # while com flag
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break # Interrompendo o looping
    s += n
    c = c + 1
##print('A soma vale {}'.format(s))
print(f'A soma vale {s}') # Interpolacao de strings
print(f'A quantidade de numeros digitados foi de {c}')