s = list(input())

result = []
num = 0

for x in s:
    # 알파벳 체크 isalpha...
    if x.isalpha():
        result.append(x)
    else:
        num += int(x)

result.sort()

if num != 0:
    result.append(str(num))

# 문자열 합치는 메소드 join 기억...
print(''.join(result))