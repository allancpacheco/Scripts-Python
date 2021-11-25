num = int(input('Digite um numero para a conversao '))

base = input('''Selecione a base de conversao
                B = Binario
                O = Octal
                H = Hexadecimal ''')

if (base == 'B'):
    print('Conversao em binario do numero = {}'.format(bin(num)))
elif(base == 'O'):
    print('Conversao em Octal do numero = {}'.format(oct(num)))
elif (base == 'H'):
    print('Conversao em Hexadecimal do numero {}'.format(hex(num)))
else:
    print('Opcao invalida')