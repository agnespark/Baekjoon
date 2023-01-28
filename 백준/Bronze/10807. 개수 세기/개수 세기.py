num = int(input())
count = 0

nums = list(map(int, input().split()))
find_num = int(input())

for i in range (num):
    if nums[i] == find_num:
        count += 1

print(count)