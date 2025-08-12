def binary_search(temperatures, target):
    # Binary search that calculates the middle index mid and compares the temperature 
    # at index mid with the target temperature.
    left, right = 0, len(temperatures)-1

    while left <= right:
        mid = (left + right) // 2
        if temperatures[mid] == target:
            return mid
        elif temperatures[mid] < target:
            left =  mid + 1
        else:
            right = mid - 1

# Setup & call
temperatures = [20, 21, 22, 22, 23, 23, 24, 25, 25, 25, 24, 23, 22, 21, 20, 19, 18, 18, 17, 16, 16, 15, 14, 13]
target_temperature = 22
index = binary_search(temperatures, target_temperature)

# If the temperature is not found after the loop, returns -1 to indicate 
# that the temperature is not present in the list of hourly temperatures.
if index != -1:
    print(f"Temperature {target_temperature} found at hour {index + 1}")
else:
    print(f"Temperature {target_temperature} not found in the hourly temperatures")
