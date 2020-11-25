N = int(input("N: "))
MaxP = 0
NumMaxP = 0


for i in range(1, N+1):
	m, v = map(int, input("m v: ").split())
	P = m / v
	if MaxP < P:
		MaxP = P
		NumMaxP = i

print('Номер детали: ', NumMaxP)
print('Плотность: ', MaxP)

#сделано


