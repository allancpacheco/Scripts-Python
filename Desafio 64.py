soma = 0
n = 0
quantidade = 0

n = int(input('Digite um numero '))

while n != int(999):
    soma = soma + n
    quantidade = quantidade + 1
    n = int(input('Digite um numero '))
    
print('A soma dos numeros foi de {}'.format(soma))
print('A quantidade de numeros digitados foi de {}'.format(quantidade))
print('A media dos numeros digitados foi de {}'.format(soma/quantidade))
