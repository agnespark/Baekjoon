n = int(input())
word = set()

for _ in range (n):
    word.add(input())

sort_word = []
for i in word:
    sort_word.append((len(i), i))

result = sorted(sort_word)

for len_word, word in result:
    print(word)