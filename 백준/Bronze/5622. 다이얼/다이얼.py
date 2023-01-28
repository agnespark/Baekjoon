alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
seconds = 0

for i in range (len(alpabet_list)):
    for j in range (len(word)):
        if word[j] in alpabet_list[i]:
            seconds += (i+2) + 1
        else:
            pass

print(seconds)
