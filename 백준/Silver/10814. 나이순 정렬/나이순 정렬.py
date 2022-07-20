n = int(input())
list1 = []

for _ in range(n):
    list1.append(input().split())

list1.sort(
    key=lambda x: int(x[0])
)

for i in list1:
    print(" ".join(i))
