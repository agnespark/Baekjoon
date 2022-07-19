a, b = map(int, input().split())

a = int(str(a)[::-1])
b = int(str(b)[::-1])
        
if a > b:
    print (a)
elif b > a:
    print (b)