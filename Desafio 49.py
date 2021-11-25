num = int(input('Digite o numero que deseja saber a tabuada: '))

for c in range(1,11):
    print('{} x {} = {}'.format(num, c, num*c))
print('Fim')