n = int(input())
sum = 0
count = 0

while True:
    count += 1
    sum += count
    if sum > n:
        break

print(count-1)
