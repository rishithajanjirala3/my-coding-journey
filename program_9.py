# Problem: Reverse the elements of the array
#using two-pointer technique
def reverse_arr(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # swap
        left += 1
        right -= 1

    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
print("Reversed:", reverse_arr(arr))
