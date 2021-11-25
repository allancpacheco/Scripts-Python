from math import hypot

ca = float(input('Digite o valor do cateto adjacente '))
co = float(input('Digite o valor do cateto oposto '))

hip = hypot(ca,co)

print('O valor da hipotenusa e de {}'.format(hip))