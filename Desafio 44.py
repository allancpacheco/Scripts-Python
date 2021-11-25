valor = int(input('Digite o valor da mercadoria R$ '))
forma_pag = int(input('''Digite a forma de pagamento:
                  1 -  Dinheiro/ Cheque
                  2 -  Cartao de Credito a vista
                  3 -  Cartao de Credito ate 2 x 
                  4 -  Cartao de credito 3 x ou mais + 
                  '''))

if(forma_pag == 1):
    novo_valor = valor - (valor * 0.10)
    print ('O valor a pagar com 10 porcento de desconto e de R$ {:.2f}'.format(novo_valor))

elif(forma_pag == 2):
    novo_valor = valor - (valor * 0.05)
    print ('O valor a pagar com 5 porcento de desconto e de R$ {:.2f}'.format(novo_valor))

elif(forma_pag == 3):
    parcela = int(input('Digite a quantidade de parcelas: '))
    if(parcela == 1):
        novo_valor = valor - (valor * 0.05)
        print ('O valor a pagar com 5 porcento de desconto e de R$ {:.2f}'.format(novo_valor))
    elif(parcela == 2):
        novo_valor = valor / 2
        contador = 1
        print('O valor sera pago em 2 parcelas de:')
        while(contador <= parcela):
            print('{} parcela de {:.2f}'.format(contador,novo_valor))
            contador = contador + 1
    else:
        print('Numero de parcelas incorreto para essa opcao')
elif(forma_pag == 4):
    parcela = int(input('Digite a quantidade de parcelas: '))
    contador = 1
    novo_valor = (valor + (valor * 0.20)) / parcela
    while(contador <= parcela):
       print('{} parcela de {:.2f}'.format(contador,novo_valor))
       contador = contador + 1 
else:
    print ('Opcao incorreta')