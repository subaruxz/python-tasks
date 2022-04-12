N = 3
M = 4

A = [
[12,11,9,10],
[8, 7, 6, 5],
[4, 3, 2, 1]]

for i in range(N):
i min = 0
v min = A[i][0]
for j in range(M):
if A[i][j] < v min:
i min = j
v min = A[i][j]
tmp = A[i][0]
A[i][0] = A[i][i min]
A[i][i min] = tmp

for i in range(N):
i max = 0
v max = A[i][0]
for j in range(M):
if A[i][j] > v max:
i max = j
v max = A[i][j]
tmp = A[i][M-1]
A[i][M-1] = A[i][i max]
A[i][i max] = tmp

for i in range(N):
for j in range(M):
print("%2d " % A[i][j], end='')
print()