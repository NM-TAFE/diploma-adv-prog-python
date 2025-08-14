def merge_sort(arr):
    if len(arr) > 1:
        mid_point = len(arr) // 2
        LEFT = arr[:mid_point]
        RIGHT = arr[mid_point:]

        merge_sort(LEFT)
        merge_sort(RIGHT)

        #set the starting point
        index_left = index_right = target_index = 0

        while index_left < len(LEFT) and index_right < len(RIGHT):
            if LEFT[index_left] < RIGHT[index_right]:
                arr[target_index] = LEFT[index_left]
                index_left += 1
            else:
                arr[target_index] = RIGHT[index_right]
                index_right += 1
            target_index += 1

        # swap
        while index_left < len(LEFT):
            arr[target_index] = LEFT[index_left]
            index_left += 1
            target_index += 1

        while index_right < len(RIGHT):
            arr[target_index] = RIGHT[index_right]
            index_right += 1
            target_index += 1

    return arr

# Example usage
print(merge_sort([64, 34, 25, 12, 22, 11, 90]))
