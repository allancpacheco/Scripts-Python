salario = float(input("Digite seu salario R$ "))

if(salario > 1250):
    novo_salario = salario + (salario * 0.10)
else:
    novo_salario = salario + (salario * 0.15)
print('O novo salario e de {}'.format(novo_salario))