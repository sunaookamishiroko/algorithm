n = int(input())
arr = list(map(int, input().split()))

arr.sort()

value = 1

for x in arr:
    if value < x:
        break
    value += x

print(value)