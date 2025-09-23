import random
SIZE = 1000

unsorted = [random.randint(0, 10000) for _ in range(SIZE)]

def sort_quickly(arr, counter = 0):
    if len(arr) <= 1:
        return arr
    if counter:
        print(counter)
    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return sort_quickly(left) + [pivot] + sort_quickly(right, counter=counter+1)

unsorted.sort()
sort_quickly(unsorted)