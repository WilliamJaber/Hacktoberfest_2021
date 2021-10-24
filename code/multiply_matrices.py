
# Pass Matrix 1 3x4
A = [[5,1,9,10],
    [21,7,1,4],
    [1,2,3,4]]

# Pass Matrix 2 3x3
B = [[6,2,10],
    [2,5,11],
    [8,2,3]]

# The result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

for i in range(len(B)):
   for j in range(len(A[0])):
       for k in range(len(B)):
           result[i][j] += B[i][k] * A[k][j]

for r in result:
   print(r)