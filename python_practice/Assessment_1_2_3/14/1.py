import numpy as np

arr = [
 [1,2,3,4],
 [5,6,7,8],
 [1,2,3,4],
 [5,6,7,8]
]

numpy_arr = np.array(arr)

transpose = numpy_arr.T

print(transpose.tolist())