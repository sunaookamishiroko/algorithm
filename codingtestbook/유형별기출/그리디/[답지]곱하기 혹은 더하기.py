arr = list(map(int, input()))

result = arr[0]

for x in range(1, len(arr)):
    if arr[x] <= 1:
        result += arr[x]
    else:
        result *= arr[x]

print(result)