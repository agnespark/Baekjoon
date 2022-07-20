a = int(input())
case_list = []

for _ in range (a):
    case_list.append(list(map(int, input().split())))

for case in case_list:
    sum = 0
    avg = 0

    cnt =0
    for c in case[1:]:
        sum += c
    avg = sum/(len(case)-1)

    for c in case[1:]:
        if c > avg:
            cnt += 1

    print(f'{cnt/(len(case)-1)*100:.3f}%')