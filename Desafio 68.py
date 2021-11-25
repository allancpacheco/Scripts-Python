import random 

jogadas = 0

while True:

    num_jog = int(input('Digite um numero para jogar: '))
    opcao_jog = str(input('Digite a opcao (I = Impar /P = Par)')).strip().upper()[0]
    num_com = random.randint(0,10)
    opcao_ganha = ' '

    print('Voce jogou {}, o computador jogou {}.Deu {}'.format(num_jog, num_com, num_jog + num_com))

    if (num_jog + num_com) % 2 == 0:
       print('-='*50)
       print('Par Ganhou')
       print('-='*50)
       opcao_ganha = 'P'
    else:
       print('-='*50)
       print('Impar ganhou')
       print('-='*50)
       opcao_ganha = 'I'

    if opcao_ganha == opcao_jog:
        print('-='*50)
        print('Voce ganhou a rodada')
        print('-='*50)
        jogadas = jogadas + 1
    else:
        print('Voce perdeu a rodada')
        print('-='*50)
        print('Voce conseguiu ganhar {} jogadas'.format(jogadas))
        print('-='*50)
        break


    


