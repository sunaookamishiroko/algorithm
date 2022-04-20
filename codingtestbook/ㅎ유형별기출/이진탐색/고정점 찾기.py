n = int(input())
data = list(map(int, input().split()))


def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2

        if data[mid] == mid:
            return mid

        if data[mid] > mid:
            end = mid - 1
        elif data[mid] < mid:
            start = mid + 1
    return -1


print(binary_search(0, n-1))