word = input()
word_list = list(('abcdefghijklmnopqrstuvwxyz'))

for i in word_list:
    if i in word:
        print(word.index(i), end=' ')
    else:
        print( -1, end=' ')
