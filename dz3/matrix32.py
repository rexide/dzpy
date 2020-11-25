matrix = [[1,2,4,-3],[4,5,7,-6],[7,0,8,-9]]
result = 0
for i, line in enumerate(matrix):
    len_positive = len(list(filter(lambda x : x >0, line)))
    if (len(line) - line.count(0)) == len_positive:
        result = i+1
        break
print(result)