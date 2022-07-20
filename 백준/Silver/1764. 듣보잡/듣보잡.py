n, m = map(int, input().split())
list1 = set()
list2 = set()

for _ in range (n):
    list1.add(input())

for _ in range (m):
    list2.add(input())

list3 = sorted(list(list1 & list2))
print(len(list3))

for i in list3:
    print(i)