import heapq

n = int(input())
heap = []
for x in range(n):
    card = int(input())
    heapq.heappush(heap, card)

hap = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    hap += one + two
    heapq.heappush(heap, one + two)

print(hap)