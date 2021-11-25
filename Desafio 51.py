p = int(input('Digite o primeiro elemento da PA: '))
r = int(input('Digite a razao da PA: '))
q = 10

s = 1

u = p + (q-1)*r
u = u + 1

for c in range(p, u, r):
    print(c, end = ' - ')
    
