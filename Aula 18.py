'''dados = list()

dados.append('Pedro')

dados.append(25)

print(dados[0])

pessoas = list()

pessoas.append(dados[:]) ## copia de dados da estrutura (lista da lista)

print(pessoas[0][0])'''

'''teste = list()
teste.append('Allan')
teste.append('32')
galera = list()
galera.append(teste[:]) ## adiciona na lista com [:]
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) ## adiciona na lista com [:]
print(galera)'''

##galera = [['Joao', 19],['Ana',33],['Joaquim',13],['Maria', 45]] ## Declarando lista dentro de listas

##print(galera[2][1]) ## Acessando os itens

##for p in galera: ## usando for para acessar os dados
##    print(f'{p[0]} tem a idade de {p[1]} anos') ## acessando e formatando a saida.

galera = list()
dado = list()

totmaior = totmenor = 0

for c in range(0,3):
    dado.append(str(input('Nome: '))) ## insere dado[0]
    dado.append(int(input('Idade: '))) ## insere dado [1]
    galera.append(dado[:]) ## cria a copia de dado dentro de galera
    dado.clear() ## limpa a lista dado

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} e maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} e menor de idade')
        totmenor += 1

print(f'Temos {totmaior} maior de idade')
print(f'Temos {totmenor} menor de idade')





