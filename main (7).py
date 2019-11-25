from random import random
N = 5
a = []
m1 = 0
for i in range(N):
    b = []
    for j in range(N):
        b.append(int(random()*25)-15)
        print('%4d' % b[j], end='')
    print()
    a.append(b)
print()

for i in range(N):
    m2 = max(a[i])
    if m2 > m1:
        m1 = m2

print()
print('Наибольший элемент в матрице', m1)
print()

for i in range(N):
    for j in range(N):
        if a[i][j] == m1:
            print('Индекс наибольшего элемента в матрице: ',(i + 1, j + 1))