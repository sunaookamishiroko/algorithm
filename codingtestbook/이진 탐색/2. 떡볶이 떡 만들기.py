n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for x in arr:
        if x > mid:
            temp += x - mid

    if temp >= m:
        result = mid
        start = mid + 1
    elif temp < m:
        end = mid - 1

print(result)