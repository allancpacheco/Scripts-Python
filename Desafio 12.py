preco = float(input("Digite o preco do produto R$"))

preco_desconto = ((preco * 0.05) - preco) *-1

print("O valor do produo com 5% de desconto e de R${:.2f}".format(preco_desconto))