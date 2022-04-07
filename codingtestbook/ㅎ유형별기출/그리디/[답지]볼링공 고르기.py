n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = [0] * 11

result = 0

for x in arr:
    count[x] += 1

for i in range(1, m + 1):
    n -= count[i]   # 무게가 i인 볼링공의 개수 제외
    result += count[i] * n # B가 선택하는 경우의 수와 곱하기