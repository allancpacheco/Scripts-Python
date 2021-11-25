numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis','Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze','Treze', 'Quatorze', 'Quinze', 'Dezesseis','Dezessete','Dezoito','Dezenove', 'Vinte')

while True:
    n = int(input('Digite um numero: '))
    if n > 0 and n < 20:
        print('Voce digitou o numero {}'.format(numeros[n]))
    else:
        print('Numero nao encontrado tente novamente')