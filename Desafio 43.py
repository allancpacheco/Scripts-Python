altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / altura**2

if(imc <= 18.5):
    print('Seu IMC e de {:.2f} e voce esta abaixo do peso'.format(imc))
elif(imc > 18.5) and (imc <= 25):
    print('Seu IMC e de {:.2f} e voce esta no peso ideal'.format(imc))
elif(imc > 25) and (imc <= 30):
    print('Seu IMC e de {:.2f} e voce esta com sobrepeso'.format(imc))
elif(imc > 30) and (imc <= 40):
    print('Seu IMC e de {:.2f} e voce esta com sobrepeso'.format(imc))
elif(imc > 40):
    print('Seu IMC e de {:.2f} e voce esta com obesidade morbida'.format(imc))
