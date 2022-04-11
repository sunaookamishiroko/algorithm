# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
#
# result = []
#
# for x in range(1, arr[-1] + 1):
#     answer = 0
#     for y in range(len(arr)):
#         answer += abs(x - arr[y])
#
#     result.append(answer)
#
# print(result.index(min(result)) + 1)

# 항상 중간값에 안테나를 설치하는것이 최소이다..
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(arr[(n-1) // 2])