import random


def create_arr(start, end, count, repeat_allowed=True, sort=True):
    arr = []

    if not repeat_allowed and (end - start + 1) <= count:
        raise Exception('Can not create a random list with given condition.')

    while len(arr) < count:
        item = random.randint(start, end)
        if repeat_allowed:
            arr.append(item)
        else:
            if item not in arr:
                arr.append(item)

    if sort:
        arr.sort()

    return arr


def seek(arr, target):
    tries = 0

    left_index = 0
    right_index = len(arr) - 1

    while left_index <= right_index:
        tries += 1
        mid_index = (left_index + right_index) // 2

        if arr[mid_index] == target:
            return (mid_index, tries)
        elif target < arr[mid_index]:
            right_index = mid_index - 1
        else:
            left_index = mid_index + 1
    
    return (-1, tries)

# arr = create_arr(1, 100, 50, repeat_allowed=False)
# print(arr)
# print(seek(arr, 70))
