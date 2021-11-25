velocidade = float(input("Digite a velocidade do carro: "))

if(velocidade <= 80):
    print("O carro nao teve multas")
else:
    velocidade_maior = velocidade  - 80
    multa = velocidade_maior * 7
    print("O carro exedeu a velocidade maxima da via, a multa e de R${:.2f}".format(multa))