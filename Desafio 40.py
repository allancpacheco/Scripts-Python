nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if(media < 5):
    print('Sua media foi de {} e voce esta REPROVADO'.format(media))
elif(media > 7):
    print('Sua media foi de {} e voce esta APROVADO'.format(media))
elif(media > 5) and (media < 6.9):
    print('Sua media foi de {} e voce esta de RECUPERACAO'.format(media))