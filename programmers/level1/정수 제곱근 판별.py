import math

def solution(n):
    num = math.sqrt(n)
    if num % int(num) == 0.0:
        return (int(num) + 1)**2
    else:
        return -1