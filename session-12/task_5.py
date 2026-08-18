
#map()
num = [40, 60, 80, 120]



result = list(map(lambda x: x * 2, num))
print(result)

#filter()
num_1 = result
result_1 = list(filter(lambda x: x > 100 ,num_1))
print(result_1)

num_2 = result_1


#reduce() 
from functools import reduce

result_2 = reduce(lambda x, y: x+y,num_2)
print(result_2)