km = int(input('Digite a quantidade de quilometros rodados com o carro '))
dias = int(input('Digita a quantidade de dias que o cliente ficou com o carro '))

total_pagar = (km * 0.15) + (dias * 60)

print("O total a pagar pelo uso do carro e de R$ {}".format(float(total_pagar)))