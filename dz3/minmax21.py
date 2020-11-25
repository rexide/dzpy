import random
 
 
def ever(n):
    if n > 2:
        mlist = [random.randint(1, 20) for i in range(n)]
        print(*mlist)
        sr = sum(mlist) / len(mlist)
        print(sr)
    else:
        print('неверное число')
 
 
if __name__ == '__main__':
    ever(n=5)

#сделано