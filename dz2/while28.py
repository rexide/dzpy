e = int(input("Введите число e: "))
Ak1 = 0
Ak = 2
K = 1
k = 1

while abs(Ak-Ak1) >= e:
	k += 1
	Ak1 = Ak
	Ak = 2 + 1 / Ak1

print(k, Ak1, Ak)