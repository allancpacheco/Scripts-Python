
opcao = 'S'
maior = menor = cont = soma = 0

while opcao in 'Ss':
    numero = int(input('Digite um numero '))
    cont = cont + 1
    soma = soma + numero
    
    if cont == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    opcao = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
    

media = soma / cont
print('O menor numero digitado foi {}'.format(menor))
print('O maior numeto digitado foi {}'.format(maior))
print('A soma dos numeros digitados {}'.format(soma))
print('A media dos numeros e de {:.2f}'.format(media))


    