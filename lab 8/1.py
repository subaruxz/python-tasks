N = 3

A = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

c = 0
s = 0
for i in range(N):
for j in range(i + 1, N):
if A[i][j] > 0:
s += A[i][j]
c += 1

print("count:",c)
print("sum:",s)