valor = float(input('Qual e o valor do imovel ? '))
salario = float(input('Qual e o seu salario ? '))
prazo = float(input('Em quantos anos voce vai pagar ? '))

prestacao = valor / prazo

salario_30 = salario * 0.30

if(prestacao > salario_30):
    print('Infelizmente seu emprestimo foi negado devido a 1/3 do seu salario = {} ser menor que a prestacao de {}'.format(salario_30, prestacao))
else:
    print('Parabens seu emprestimo foi aprovado')