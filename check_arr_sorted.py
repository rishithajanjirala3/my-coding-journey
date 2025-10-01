# Problem: Check if the array is sorted in non-decreasing order

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

# Example usage
arr = [1, 2, 3, 4, 5]
print("Is sorted?", is_sorted(arr))
