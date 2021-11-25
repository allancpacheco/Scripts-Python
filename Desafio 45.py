import random

jogador = int(input('''Digite a opcao
                       1 - Pedra
                       2 - Papel
                       3 - Tesoura 
                       '''))

if(jogador > 3):
    print('Opcao invalida')
if(jogador < 0):
    print('Opcao invalida')

lista = [1,2,3]
nomes = ['Pedra','Papel','Tesoura']
computador = random.choice(lista)

print('Voce jogou: {}'.format(nomes[jogador - 1]))
print('Computador jogou: {}'.format(nomes[computador - 1]))

if (computador == jogador):
    print('Empatou !!!!')
elif(computador == 1) and (jogador == 2):
    print('Voce Venceu')
elif(computador == 1) and (jogador == 3):
    print('Computador Venceu')
elif(computador == 2) and (jogador == 1):
    print('Computador Venceu')
elif(computador == 2) and (jogador == 3):
    print('Voce Venceu')
elif(computador == 3) and (jogador == 1):
    print('Voce Venceu')
elif(computador == 3) and (jogador == 2):
    print('Computador Venceu')
else:
    print('Opcao incorreta')