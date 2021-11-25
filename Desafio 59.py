n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

controle = 0
soma = 0
mult = 0

while controle != 5:
    
    print('''Digite uma opcao
                 1 - Somar
                 2 - Multiplicar
                 3 - Maior
                 4 - Novos numeros
                 5 - Sair do programa
                 : ''')
    controle = int(input('Qual e a sua opcao ? '))

    if(controle == 1):
        soma = n1 + n2
        print('A soma e de {}'.format(soma))
    if(controle == 2):
        mult = n1 * n2
        print('A multiplicacao e de {}'.format(mult))
    if(controle == 3):
        if(n1 < n2):
            print('O numero {} e maior '.format(n2))
        else:
            print('O numero {} e maior '.format(n1))
    if(controle == 4):
        print('Digite novos numeros:')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
