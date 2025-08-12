def insertion_sort(arr):
    for current in range(1, len(arr)):
        key = arr[current]
        previous = current - 1
        while previous >= 0 and key < arr[previous]:
            arr[previous + 1] = arr[previous]
            previous -= 1
        arr[previous + 1] = key
    return arr

# Example usage
print(insertion_sort([64, 34, 25, 12, 22, 11, 90]))
