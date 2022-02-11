N, M = map(int, input().split())
answerlist = []

for i in range(N):
    cardlist = (list(map(int, input().split())))
    answerlist.append(min(cardlist))

print(max(answerlist))