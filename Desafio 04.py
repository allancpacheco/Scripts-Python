n = input("Digite algo ")

print('E um numero {} ?'.format(n.isalnum()))
print('E alfamumerico {} ?'.format(n.isalpha()))
print('E um Ascii ? {}'.format(n.isascii()))
print('E um numero decimal ? {}'.format(n.isdecimal()))
print('E um digito ? {}'.format(n.isdigit()))
print('E um identificador ? {}'.format(n.isidentifier()))
print('E numerico ? {}'.format(n.isnumeric()))