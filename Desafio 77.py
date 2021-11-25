palavras = ('aprender','programar','linguagem',
'python','curso','gratis','estudar','praticar',
'trabalhar','mercado','programador','futuro')

for p in palavras: # analisa as palavras nas tuplas
    print(f'\nNa palavra {p.upper()} temos', end = ' ')
    for letra in p: # analista as letras de cada palavra da tupla
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
