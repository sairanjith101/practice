X = [
 [1,2,3,4],
 [5,6,7,8],
 [1,2,3,4],
 [5,6,7,8]
]

matrix = [[X[column][row] for column in range(len(X))]
          for row in range(len(X[0]))]

for mat in matrix:
    print(mat)