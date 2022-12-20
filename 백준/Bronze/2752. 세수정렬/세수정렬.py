num = input().split()
num = list(map(int, num))

if (num[0] > num[2]):
    temp = num[0]
    num[0] = num[2]
    num[2] = temp

if (num[0] > num[1]):
    temp = num[0]
    num[0] = num[1]
    num[1] = temp

if (num[1] > num[2]):
    temp = num[1]
    num[1] = num[2]
    num[2] = temp

print(num[0], num[1], num[2])
