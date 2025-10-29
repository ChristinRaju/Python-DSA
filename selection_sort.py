def selection_sort(arr):
    """Sorts an array using the selection sort algorithm.

    Args:
        arr (list): A list of elements to be sorted.

    Returns:
        list: A new list containing the sorted elements.
    """
    n = len(arr)
    sorted_arr = arr.copy()

    for i in range(n):
        # Assume the minimum is the first element of the unsorted part
        min_index = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        sorted_arr[i], sorted_arr[min_index] = sorted_arr[min_index], sorted_arr[i]

    return sorted_arr

nums = [64, 25, 12, 22, 11]
print("Original array:", nums)

sorted_nums = selection_sort(nums)
print("Sorted array:", sorted_nums)

"""Output:
Original array: [64, 25, 12, 22, 11]
Sorted array: [11, 12, 22, 25, 64]  
"""

# Explanation of each pass:
# Pass 1 → [11, 25, 12, 22, 64]
# Pass 2 → [11, 12, 25, 22, 64]
# Pass 3 → [11, 12, 22, 25, 64]
# Pass 4 → [11, 12, 22, 25, 64]
# Pass 5 → [11, 12, 22, 25, 64]
