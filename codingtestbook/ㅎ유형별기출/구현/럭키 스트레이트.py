n = list(map(int, input()))
length = len(n) // 2

num1 = 0
num2 = 0

for x in range(length):
    num1 += n[x]
    num2 += n[length + x]

if num1 == num2:
    print("LUCKY")
else:
    print("READY")