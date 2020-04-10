def find_max(data):
    """ Return the maximum element from a nonempty Python list.
    从非空Python列表中返回最大元素。 """
    biggest = data[0]       # The initial value to beat
    for val in data:        # For each value:
        if val > biggest:   # if it greater than the best so far,
            biggest = val   # we have found a new best (so far)
    return biggest          # When loop ends, biggest is the max

print(find_max([12, 45, 3, 78, 9, 8, 7,89]))
