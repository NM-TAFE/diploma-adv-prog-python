def selection_sort(arr):
    # outer loop ensures we move up the array and place the items at the ealiest position
    for index in range(len(arr)):
        current_index = index
        for next_index in range(index+1, len(arr)):
            if arr[next_index] < arr[current_index]:
                # if next is greater move the index and swap
                current_index = next_index
                arr[index], arr[current_index] = arr[current_index], arr[index]
    return arr

# Example usage
print(selection_sort([64, 34, 25, 12, 22, 11, 90]))
