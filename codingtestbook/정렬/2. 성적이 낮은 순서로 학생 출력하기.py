n = int(input())
arr = []

for x in range(n):
    name, score = input().split()
    arr.append((name, int(score)))

for item in sorted(arr, key=lambda student: student[1]):
    print(item[0], end=' ')