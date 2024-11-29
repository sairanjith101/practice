X = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [1, 2, 3, 4],
     [5, 6, 7, 8]]

result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# # Python Program to Transpose a Matrix using the list comprehension

rez = [[X[column][row] for column in range(len(X))]
    for row in range(len(X[0]))]

for row in rez:
   print(row)
