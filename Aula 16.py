#lanche = 'Hamburguer'
#lanche = 'Suco'
## lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
## Tupla sao imutaveis 
# Exemplo: lanche[1] = 'Refrigerante'
## print(lanche)

##print(sorted(lanche)) ## Organiza a lista sem alterar
##print(lanche)

# Se nao precisar mostrar a posicao.
'''for comida in lanche:
    print('Eu vou comer {}'.format(comida))

print('-='*50)

for cont in range(0,len(lanche)):
    print('Eu vou comer {} na posicao {}'.format(lanche[cont], cont)) # mostrando o conteudo da variavel

print('-='*50)

for pos, c in enumerate(lanche): # for dentro da lista
    print('Eu vou comer {} na posicao {}'.format(c,pos))

print('Comi pra caramba')'''

'''a = (2,5,4)
b = (5,8,1,2)
c = a + b

print(c.count(5)) # contagem de elemento

print(c.index(2)) #posicao do elemento

print(c.index(2,4)) # posicao do elemento com deslocamento'''

pessoa = ('Gustavo', 39, 'M', 99.88)
# del(pessoa) ## apagando a variavel
# del(pessoa[1]) # nao e possivel deletar apenas um elemento na tupla
print(pessoa)







