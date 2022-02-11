N, M = map(int, input().split())
answerlist = []
# answer = 0
for i in range(N):
    cardlist = (list(map(int, input().split())))
    answerlist.append(min(cardlist))
    # answer = max(answer, min(cardlist))

# print(answer)
print(max(answerlist))