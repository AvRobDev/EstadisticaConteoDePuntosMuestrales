import math
from functools import reduce
from operator import mul 

def punteo_muestral(n, *subgroups_size):
     numerator = math.factorial(n)

     denominator = reduce(mul, (math.factorial(size) for size in subgroup_sizes), 1)
    
     result = numerator // denominator
    
     return result

n = 4
subgroup_sizes = [1, 1, 1, 1]
result = punteo_muestral(n, *subgroup_sizes)
print(result)