arr = list(map(int, input()))

count0 = 0
count1 = 0

if arr[0] == 0:
    count0 += 1
else:
    count1 += 1

before = arr[0]

for x in range(1, len(arr)):
    if before != arr[x]:
        if arr[x] == 0:
            count0 += 1
        else:
            count1 += 1
        before = arr[x]

print(min(count0, count1))