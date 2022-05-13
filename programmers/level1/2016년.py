def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days = 0

    for x in range(a - 1):
        days += month[x]
    days += b
    return day[days % 7 - 1]