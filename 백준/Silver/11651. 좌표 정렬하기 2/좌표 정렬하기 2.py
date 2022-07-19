n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((b,a))

arr.sort()

for b, a in arr:
    print(a,b)