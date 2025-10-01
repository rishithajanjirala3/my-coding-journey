# Problem: Find the maximum and minimum elements in the array

def find_max_min(arr):
    if not arr:
        return None, None  # handle empty array

    maximum = arr[0]
    minimum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum

# Example usage
arr = [10, 5, 3, 9, 20, 2]
max_val, min_val = find_max_min(arr)
print("Max:", max_val)
print("Min:", min_val)
