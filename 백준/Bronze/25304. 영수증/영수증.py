total_price = int(input())
total_goods = int(input())

sum = 0 

for i in range(total_goods):
    good = input().split()
    sum += (int(good[0]) * int(good[1]))

if total_price == sum:
    print("Yes")
else:
    print("No")