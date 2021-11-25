ano = int(input("Digite o ano: "))

if(ano % 4 == 0):
    print("o ano de {} e um ano bissexto".format(ano))
else:
    print("o ano de {} NAO e um ano bissexto".format(ano))