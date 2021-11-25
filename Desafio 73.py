times = ('Atlético-GO',
'Atlético-MG',
'Bahia',
'Botafogo',
'Bragantino',
'Ceará',
'Corinthians',
'Coritiba',
'Flamengo',
'Fluminense',
'Fortaleza',
'Goiás',
'Grêmio',
'Internacional',
'Palmeiras',
'Santos',
'São Paulo',
'Sport',
'Vasco')


print(sorted(times)) # 0rdem alfabetica
print('-='*50) 
print(times[:5])
print('-='*50)
print(times[len(times) - 5 :len(times)])
print('-='*50)
print('O Gremio esta na {} posicao'.format(times.index('Grêmio'))) #posicao do elemento