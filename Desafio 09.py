
num = int(input("Digite um numero: "))

print('{} x {} = {}'.format(num, int(1), num*int(1)))
print('{} x {} = {}'.format(num, int(2), num*int(2)))
print('{} x {} = {}'.format(num, int(3), num*int(3)))
print('{} x {} = {}'.format(num, int(4), num*int(4)))
print('{} x {} = {}'.format(num, int(5), num*int(5)))
print('{} x {} = {}'.format(num, int(6), num*int(6)))
print('{} x {} = {}'.format(num, int(7), num*int(7)))
print('{} x {} = {}'.format(num, int(8), num*int(8)))
print('{} x {} = {}'.format(num, int(9), num*int(9)))
print('{} x {} = {}'.format(num, int(10), num*int(10)))

print('Usando o While')

contador = 1

while (int(contador) <= 10):
    print('{} x {} = {}'.format(num, contador, contador * num))
    contador = contador + 1