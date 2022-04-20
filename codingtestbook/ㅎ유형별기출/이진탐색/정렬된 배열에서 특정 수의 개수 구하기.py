from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))

left = bisect_left(data, x)
right = bisect_right(data, x)

if left == n:
    print(-1)
else:
    print(right-left)