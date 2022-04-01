n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for x in range(k):
    A[A.index(min(A))], B[B.index(max(B))] = B[B.index(max(B))], A[A.index(min(A))]

sum = 0
for item in A:
    sum += item

print(sum)