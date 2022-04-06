arr = list(map(int, input()))

result = 0

if arr[0] <= 1:
    result = arr[0] + arr[1]
else:
    result = arr[0] * arr[1]

for x in range(2, len(arr)):
    if arr[x] <= 1:
        result += arr[x]
    else:
        result *= arr[x]

print(result)