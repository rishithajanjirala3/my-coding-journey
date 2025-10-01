# Problem:
# Count how many even and odd numbers are present in a given array

def count_even_odd(arr):
    even_count = 0
    odd_count = 0

    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even, odd = count_even_odd(arr)

print("Even numbers:", even)
print("Odd numbers:", odd)
