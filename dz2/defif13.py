a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))


def average():
	if a > b and a > c:
		if  c > b:
			print("Среднее:", c)
		else:
			print("Среднее:", b)
	elif b > c and b > a:
		if c > a:
			print("Среднее:", c)
		else:
			print("Среднее:", a)
	elif c > a and c > b:
		if a > b:
			print("Среднее:", a)
		else:
			print("Среднее:", b)

average()