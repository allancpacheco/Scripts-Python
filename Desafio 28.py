import random

num_rd = int(random.randint(1,5))
num_es = int(input('Digite um numero de 1 a 5: '))

if(num_rd == num_es):
    print('Numero do computador {} e numero escolhido {} , voce acertou !!!!'.format(num_rd, num_es))
else:
    print('Numero do computador {} e numero escolhido {} , tente novamente !!!!'.format(num_rd, num_es))
