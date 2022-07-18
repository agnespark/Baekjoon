import sys

n = int(input())
number_list = []
for i in range (n):
    number_list.append(int(sys.stdin.readline()))
                       
number_list.sort()
                       
for j in number_list:
    print(j)