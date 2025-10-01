# Problem: Move all zeros in the array to the end 
# maintaining the order of non-zero elements

def move_zeros(arr):
    c = 0  # position to place next non-zero element

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[c], arr[i] = arr[i], arr[c]
            c += 1

    return arr

# Example usage
arr = [0, 1, 0, 3, 12]
print("After moving zeros:", move_zeros(arr))
