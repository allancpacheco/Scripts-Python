idade = homem = mulher_menos_20 = pessoas_maior_18 = 0

while True:
    print('-='*50)
    print('CADASTRO DE PESSOA')
    print('-='*50)
    idade = int(input('Digite a idade da pessoa : '))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]
        if(sexo == 'F') and idade > 20:
           mulher_menos_20 = mulher_menos_20 + 1
        if (sexo == 'M'):
           homem = homem + 1
        if idade > 18:
           pessoas_maior_18 = pessoas_maior_18 + 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar ?? (S/N) ')).strip().upper()[0]
    if opcao == 'N':
           break

print('-='*50)       
print('O total de pessoas maiores de 18 anos foi de {}'.format(pessoas_maior_18))
print('O total de mulheres menores de 20 anos foi de {}'.format(mulher_menos_20))
print('O total de homens cadastrados foi de {}'.format(homem))