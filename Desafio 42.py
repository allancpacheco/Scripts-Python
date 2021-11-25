r1 = int(input("Digite o valor da primeira reta: "))
r2 = int(input("Digite o valor da segunda reta: "))
r3 = int(input("Digite o valor da terceira reta: "))

if (r1 + r2 <= r3):
     print("NAO pode formar um triangulo")
elif (r1 + r3 <= r2):
     print("NAO pode formar um triangulo")
elif (r2 + r3 <= r1):
     print("NAO pode formar um triangulo")
else:
    print("Pode formar um triangulo")
    if(r1 == r2) or (r1 == r3) or (r2 == r3):
        print("Forma um triangulo Isoceles")
    elif (r1 == r2) and (r2 == r3):
        print("Forma um triangulo escaleno")
    else:
        print("Forma um triangulo Equilatero")
    