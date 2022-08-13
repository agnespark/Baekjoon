w=[]
k=[]
for i in range (0,10):
    w.append(int(input()))

for i in range (0,10):
    k.append(int(input()))

w.sort(reverse=True)
k.sort(reverse=True)

wsum = 0
ksum = 0
for i in range(0, 3):
    wsum += w[i]
    ksum += k[i]
print(wsum, ksum)