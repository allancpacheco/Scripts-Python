from random import randint

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Os valores sorteados foram ', end='')
for c in n:
    print(f'{c}',end=' ')

print(f'\nO maior numero sorteado foi {max(n)}')
print(f'O menor numero sorteado foi {min(n)}')