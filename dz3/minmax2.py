Min = a[1]
Max = [1]
s = a[1]
N = int(input("N: "))
for i in range(1, N+1):
	R = int(input(str(i) + " элемент: "))
	Min = a[1]
	Max = [1]
	s = a[1]
	s = s + a[i]
	if a[i] < Min:
		Min = a[i]
	else:
		if a[i] > Max:
			Max = a[i]

s = (s - Min - Max)/(N-2)
print(s)