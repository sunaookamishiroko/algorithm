N, M = map(int, input().split())
cardlist = []
answerlist = []

for i in range(N):
    cardlist.append(list(map(int, input().split())))

for cards in cardlist:
    answerlist.append(min(cards))

print(max(answerlist))