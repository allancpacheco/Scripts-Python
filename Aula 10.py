## Final de codigo condicional sempre colocar ":" para destacar o inicio do bloco
## Todo comando alinhado a esquerda sempre sera executado

# Forma simplificada

'''
tempo = int(input("Quantos anos tem seu carro? "))
print('Carro novo' if tempo <=3 else 'carro velho')
print('------ FIM ------ ')

# Forma com identacao

num = int(input("Digite um numero: "))
if(num >= 5):
    print("Menor que 5")
else:
    print("Maior que 5")

nome = str(input('Qual e o seu nome? '))
if nome == 'Allan':
    print('{}, que nome lindo voce tem'.format(nome))
print('Bom dia, {}'.format(nome)) ## Esse IF sempre vai acontecer


nome = str(input('Qual e o seu nome? '))
if nome == 'Allan':
    print('{}, que nome lindo voce tem'.format(nome))
else:
    print('{}, seu nome e tao normal'.format(nome))
print('Bom dia, {}'.format(nome)) ## Esse IF sempre vai acontecer

'''


