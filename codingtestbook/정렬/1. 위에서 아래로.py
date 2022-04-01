n = int(input())
arr = []

for x in range(n):
    arr.append(int(input()))

for x in sorted(arr, reverse=True):
    print(x, end=" ")