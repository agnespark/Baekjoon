a, b = map(int, input().split())
list1 = []
list2 = []
cnt = 0

for _ in range (a):
    list1.append(input())

for _ in range (b):
    list2.append(input())

for i in range (b):
    if list2[i] in list1:
        cnt += 1
    else:
        pass

print(cnt)