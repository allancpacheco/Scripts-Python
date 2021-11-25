r = int(input('Digite a quantidade de numeros da sequencia de Fibonacci '))

p = 0
s = 1
c = 0

print(p , end=' - ')
print(s , end=' - ')

while c <= r:
     t = p + s
     print(t, end=' - ')
     c= c + 1
     p = s
     s = t