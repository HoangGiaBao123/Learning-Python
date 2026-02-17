import numpy

def arrays(arr):
    reversed_arr = numpy.array(arr, float)
    return reversed_arr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
