nome = input('Qual e o seu nome ? ')

if nome == 'Allan':
    print('Que nome bonito {}'.format(nome))
elif nome == 'Carlos' or nome == 'Zenaide':
    print ('Seu nome e bem popular no Brasil {}'.format(nome))
elif nome in 'Pacheco':
    print('Esse e um sobrenome de respeito {}'.format(nome))
else:
    print('Seu nome e bem normal {}'.format(nome))
print('Tenha um bom dia {} !!!!'.format(nome))