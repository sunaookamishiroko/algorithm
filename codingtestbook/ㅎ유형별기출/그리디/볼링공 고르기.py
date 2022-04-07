n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0

for x in range(n):
    for y in range(x + 1, n):
        if arr[x] != arr[y]:
            result += 1
print(result)