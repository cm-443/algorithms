#This is an example of a binary search algorithm expressed in python.
def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

a_list = [1,4,7,9,15,18,29,36,42,53,60]
binary_search(a_list, 9)

