n = int(input())
arr = []

for x in range(n):
    arr.append(list(input().split()))

# sort 함수에 람다로 이렇게 식을 넣으면, 첫 번째 조건이 같다면 두 번째 조건..
# 두 번째 조건이 같다면 세 번째 조건... 을 활용한다. 기억해두자.
# 기본은 오름차순. -를 붙이면 내림차순이 된다.
arr.sort(key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for ele in arr:
    print(ele[0])