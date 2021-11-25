nasc = int(input('Digite o ano do seu nascimento: '))
atual = int(2021)

idade = atual - nasc

if(idade <= 9):
    print('Voce tem {} anos e esta na Categoria Mirim'.format(idade))
elif(idade > 9) and (idade <= 14) :
    print('Voce tem {} anos e esta na Categoria Infantil'.format(idade))
elif(idade > 14) and (idade <= 19) :
    print('Voce tem {} anos e esta na Categoria Junior'.format(idade))
elif(idade > 19) and (idade <= 20) :
    print('Voce tem {} anos e esta na Categoria Senior'.format(idade))
elif(idade >= 20) :
    print('Voce tem {} anos e esta na Categoria Master'.format(idade))