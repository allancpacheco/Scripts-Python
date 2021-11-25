num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))


menor = num1

if(num2 < num1):
    menor = num2
if(num3 < num1):
    menor = num3
print("O menor numero e {}".format(menor))

maior = num1

if(num2 > num1):
    maior = num2
if(num3 > num1):
    maior = num3
print("O maior numero e {}".format(maior))



