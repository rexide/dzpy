n = int(input("Введите число n: "))
S = 0
summa = 0
for i in range(1, n+1):
	num = int(input("Введите " + str(i) + " цифру и списка: "))
	S = S + num
	if num == 0:
		summa = S
		S = 0
print(summa)