frase = input('Digite uma frase: ').upper().strip() 

print('A letra A aparece em {} vezes na frase'.format(frase.count('A')))
print('A primeira posicao em que a letra A aparece na frase e na posicao {}'.format(frase.find('A')+1))
print('A ultima posicao em que a letra A aparece na frase e na posicao {}'.format(frase.rfind('A')+1))