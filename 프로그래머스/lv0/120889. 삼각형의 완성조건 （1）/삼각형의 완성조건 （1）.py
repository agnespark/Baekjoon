def solution(sides):
    max_item = max(sides)
    other_item = sides
    other_item.remove(max_item)
    if sum(other_item) > max_item:
        return 1
    else:
        return 2
