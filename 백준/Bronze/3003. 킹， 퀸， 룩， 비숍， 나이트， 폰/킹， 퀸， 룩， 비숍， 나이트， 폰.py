chess = [1,1,2,2,2,8]

input = input().split()

for i in range(6):
    print(int(chess[i])-int(input[i]), end= ' ')