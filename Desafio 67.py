r = n = c = 0

while True:
    print('-'*100)
    n = int(input('Quer ver a tabuada de qual valor ? '))
    print('-'*100)
    c = 0
    if (n < 0):
        print('Programa tabuada encerrado. Volte Sempre !!!')
        break
    while c <= 10:
        r = n * c
        print(f'{n} x {c} = {r}')
        c = c + 1   



