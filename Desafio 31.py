distancia = float(input("Digite a distancia da viajem em KM: "))

if(distancia <= 200):
    preco = distancia * 0.50 
    print('O preco da viajem e de R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45 
    print('O preco da viajem e de R${:.2f}'.format(preco))
