data = int(input())

for i in range(data):
    brains = list(map(int, input().split()))
    if brains[0] < brains[1]:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")