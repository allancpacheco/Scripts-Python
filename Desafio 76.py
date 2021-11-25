itens = ('Caneta', 0.50, 'Caderno', 5.50, 
         'Lapiseira', 1.50, 'Transferidor', 
         4.40,'Estojo', 8.00,'Livro', 8.90,
         'Compasso', 1.50, 'Mochila', 40.50,
         'Borracha',0.50, 'Lapis', 1.50)

print('=-' * 40)
print(f'{"Listagem de materiais":^40}')
print('=-' * 40)

for pos in range(0, len(itens)):
    if pos % 2  == 0:
        print(f'{itens[pos]:.<30}', end=' ')
    else:
        print(f'R${itens[pos]:>7.2f}')

print('=-' * 40)