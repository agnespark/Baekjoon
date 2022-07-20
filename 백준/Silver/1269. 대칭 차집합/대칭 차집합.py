a, b = map(int, input().split())
list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))
print(len(list1-list2)+len(list2-list1))