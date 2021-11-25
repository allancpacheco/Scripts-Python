altura = float(input("Digite a altura da parede "))
largura = float(input("Digite a largura da parede "))

metros = altura * largura
litros = metros / 2

print("Para pintar essa parede de {} m sera necessario {} litros de tinta".format(metros,litros))