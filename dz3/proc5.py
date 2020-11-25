def  RectPS(x1, y1, x2, y2, P, S):
	P = 2*(abs(x1-x2)+abs(y1-y2))
	S = abs(x1-x2)*abs(y1-y2)

	x1 = int(input("Введите x1: "))
	y1 = int(input("Введите y1: "))
	x2 = int(input("Введите х2: "))
	y2 = int(input("Введите y2: "))

	print(P, "  ", S)


RectPS()

#сделано