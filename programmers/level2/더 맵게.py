import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if scoville[0] >= K:
            return answer
        elif len(scoville) == 1 and scoville[0] < K:
            return -1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)

        heapq.heappush(scoville, min1 + min2 * 2)
        answer += 1