def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # take first element as pivot
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted array:", quick_sort(arr))
