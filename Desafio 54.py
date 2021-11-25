s = 0

for c in range(1,8):
    ano = int(input('Digite o ano de nascimento da pessoa {}: '.format(c)))
    if(2021 - ano > 18):
        s = s + 1
    else:
        s = s

print('O total de pessoas maiores de 18 foi de {} pessoas'.format(s))