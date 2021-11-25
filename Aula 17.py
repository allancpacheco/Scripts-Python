## lista sao mutaveis

'''lista = [1,2,3,4,5,6]

lista[2] = 3 ## altera um numero na lista

lista.append(7) ##inclui o ultimo item a lista

lista.insert(0,0) ## inserir na lista 
lista.pop() ## remove o ultimo elemento
lista.remove(3) ##remove o item da lista
del lista[3] #remove o item da lista

## condicao para a remocao
if 2 in lista:
    lista.remove(2) ## remove somente a primeira ocorrencia

## criando uma lista
valores = list(range(4,11))

valores.sort() ## ordenacao de valores
valores.sort(reverse=True) ## ordenacao de valores

len(valores) ## quantidade de elementos na lista

print(valores)

valores =[] ## declarando a lista vazia.

for cont in range(0,5):
    valores.append(int(input('Digite um valor: '))) ## Digitando valores e inserindo em uma lista

for c,v in enumerate(valores): # verifica a lista toda com posicao e conteudo
    print(f' Na  posicao {c} encontrei o valor {v}')
print('Cheguei ao final da lista') '''

a = [3,5,7,9]
##  b = a #clia uma ligacao entre as listas
b = a[:] # copia os itens da lista a em b 
b[2] = 8

print(f'Lista A : {a}')
print(f'Lista B : {b}')