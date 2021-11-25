

for c in range (0,10):
    print(c)

print('Com ireracao decrecente')

for c in range (10,0, - 1): ## Com iteracao
    print(c)

print('Entrou no while')
contador = 1

while(contador < 10):
    if(contador % 2 == 0):
        print('{} = Par'.format(contador))
        contador = contador + 1
    elif(contador % 2 == 1):
        print('{} = Impar'.format(contador))
        contador = contador + 1
print('Fim')