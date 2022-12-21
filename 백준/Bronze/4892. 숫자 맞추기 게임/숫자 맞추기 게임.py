idx = 1

while True:
    num0 = int(input())

    if num0 == 0:
        break

    num1 = num0 * 3

    if num1 % 2 == 0:
        num2 = num1/2
    else:
        num2 = (num1 + 1) / 2

    num3 = num2 * 3
    num4 = num3 // 9

    if num1 % 2 == 0:
        print(f'{idx}. even {int(num4)}')
    else:
        print(f'{idx}. odd {int(num4)}')

    idx += 1
