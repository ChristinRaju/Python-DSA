def bubble_sort(arr):
    """Sorts an array using the bubble sort algorithm.

    Args:
        arr (list): A list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements.
    """
    n = len(arr)
    sorted_arr = arr.copy()

    # Traverse through all elements in the array
    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

    return sorted_arr


nums = [37, 45, 29, 8, 12]
print("Original array:", nums)

sorted_nums = bubble_sort(nums)
print("Sorted array:", sorted_nums)

"""Output:
Original array: [37, 45, 29, 8, 12]
Sorted array: [8, 12, 29, 37, 45]
"""

# Explanation of each pass:
# Pass 1 → [37, 29, 8, 12, 45]
# Pass 2 → [29, 8, 12, 37, 45]
# Pass 3 → [8, 12, 29, 37, 45]
# Pass 4 → [8, 12, 29, 37, 45]
# Pass 5 → [8, 12, 29, 37, 45]
