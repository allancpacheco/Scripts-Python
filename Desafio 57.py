s = str(input("Digite seu sexo (M = Maculino F = Feminino)" )).strip().upper()[0] ## somente a primeira letra em maiusculo

while s not in 'MmFf':
    s = str(input('Entrada invalida, digite novamente :')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(s))
