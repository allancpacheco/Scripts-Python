import random

palpite = 1
controle = ''

while controle != 'A':
    num_rd = int(random.randint(0,10))
    num_es = int(input('Digite um numero de 1 a 10: '))
    if(num_rd == num_es):
        print('Numero do computador {} e numero escolhido {} , voce acertou !!!!'.format(num_rd, num_es))
        palpite = palpite + 1
        controle = 'A'
    else:
        print('Numero do computador {} e numero escolhido {} , tente novamente !!!!'.format(num_rd, num_es))
        palpite = palpite + 1
        controle = 'E'
print('O numero de palpites foi de {} para acertar'.format(palpite))