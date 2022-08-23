round = int(input())

chang = 100
sang = 100

for i in range (0, round):
    a, b = map(int, input().split())
    if a > b:
        sang -= a
    elif a < b:
        chang -= b
    elif a == b:
        pass
print(chang)
print(sang)