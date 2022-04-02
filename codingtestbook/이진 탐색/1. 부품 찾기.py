def binary_search(arr, target, start, end):
    while start <= end:
        if start > end:
            print("no", end=' ')
            return
        mid = (start + end) // 2

        if arr[mid] == target:
            print("yes", end=' ')
            return
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    print("no", end=' ')
    return


n = int(input())
store = list(map(int, input().split()))

m = int(input())
customer = list(map(int, input().split()))

store.sort()

for element in customer:
    binary_search(store, element, 0, n-1)