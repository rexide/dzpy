k = int(input("Введите число k: "))

a = 1
b = 0

while a != 0:
	a = int(input("Введите число из набора: "))
	if a < k:
		b += 1
b -= 1
print(b)