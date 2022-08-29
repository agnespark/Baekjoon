case = int(input())

for i in range(case):
    num = int(input())
    max = 0
    school = ""

    for i in range(num):
        a, b = map(str, input().split())
        b = int(b)
        if b > max:
            max = b
            school = a

    print(school)