total = 0
p_menor = p_maior = 0
n_menor = n_maior = ''
maior_1000 = 0
cont = 1

while True:
     
     produto = str(input('Digite o nome do produto: '))
     preco = float(input('Digite o valor do produto R$'))

     total = total + preco
     print('-='*50)
     opcao = ' '

     if cont == 1:
         p_maior = preco
         n_maior = produto
         p_menor = preco
         n_menor = produto
         cont = cont + 1
     if preco > p_maior:
         p_maior = preco
         n_maior = produto
     if preco < p_menor:
         p_menor = preco
         n_menor = produto
     if preco > 1000:
        maior_1000 = maior_1000 + 1

     while opcao not in 'SN':
        opcao = str(input('Quer continuar ?? (S/N) ')).strip().upper()[0]
        print('-='*50)
     if opcao == 'N':
        break

print('O total dos produtos comprados e de R$ {}'.format(total))
print('O produto mais barato foi {} custando {}'.format(n_menor,p_menor))
print('O produto mais caro foi {} custando {}'.format(n_maior,p_maior))
print('Temos {} produtos custando mais de R$ 1000'.format(maior_1000))



