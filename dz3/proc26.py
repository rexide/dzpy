def IsPower5(K) :
    while K > 0 and K % 10 == 5 :
        K //= 5
    return K == 1 
 
my_list = [1,5,4,6,25,4,6,78,987,625]
print(sum(IsPower5(i) for i in my_list))

#сделано