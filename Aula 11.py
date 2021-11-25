## Teste com cores diretamente no terminal -- Dicionario

## Estilos

estilo_normal = 0
estilo_bold = 1
estilo_sublinhado = 4
estilo_negative = 7

## Cores letras

letra_branco = 30
letra_vermelha = 31
letra_verde = 32
letra_amarela = 33
letra_azul = 34
letra_roxa = 35
letra_piscina = 36
letra_cinza = 37

## cor de fundo

fundo_branco = 40
fundo_vermelho = 41
fundo_verde = 42
fundo_amarelo = 43
fundo_azul = 44
fundo_roxo = 45
fundo_piscina = 46
fundo_cinza = 47

print('\033[{};{};{}m Allan'.format(estilo_bold, letra_verde, fundo_azul))

##print('{}'.format(estilo_bold))

