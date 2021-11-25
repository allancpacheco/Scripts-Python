nasc = int(input('Digite o ano do seu nascimento: '))
atual = int(2021)

idade = atual - nasc

if(idade == 18):
    print('Voce esta apto para o alistamento')
elif(idade > 18):
    passou = idade - 18
    print('Seu prazo de alistamento ja passou em {} anos'.format(passou))
elif(idade < 18):
    falta = 18 - idade
    print('Ainda faltam {} anos para voce se alistar'.format(falta))