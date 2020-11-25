import random
a = [random.randint(0, 20) for i in range(10)]
print(a)
n = 0
for i in range(10):
    if (i % 2 == 0) and (a[i] % 2 == 1):
        n = a[i]
print(n)
for i in range(10):
    if a[i] % 2 == 1:
        a[i] += n
print(a)