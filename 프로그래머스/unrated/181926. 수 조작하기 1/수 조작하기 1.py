def solution(n, control):
    result = n
    for i in control:
        if i == 'w':
            result += 1
        elif i == 's':
            result -= 1
        elif i == 'd':
            result += 10
        elif i == 'a':
            result -= 10
    return result