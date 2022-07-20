r = int(input())

for _ in range (r):
    num, word = input().split()
    for i in word:    
        print(i*int(num), end='')
    print()
