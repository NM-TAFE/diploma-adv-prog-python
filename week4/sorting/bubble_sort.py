def bubble_sort(arr):
    number= len(arr)
    for outer in range(number):
        for inner in range(0, number - outer - 1): 
            if arr[inner] > arr[inner+1]:
                arr[inner], arr[inner+1] = arr[inner+1], arr[inner]
    return arr

# Example usage
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
