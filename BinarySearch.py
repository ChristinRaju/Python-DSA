# Recursive Binary Search
def binary_search(arr, low, high, key):
    if low > high:   # base case: not found
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, low, mid-1, key)
    else:
        return binary_search(arr, mid+1, high, key)

# Example array (must be sorted)
arr = [1, 3, 5, 7, 9, 11, 13]
key = 7

# Call binary_search
result = binary_search(arr, 0, len(arr)-1, key)

if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found")


#############################################################


# Iterative Binary Search
arr = [1, 3, 5, 7, 9]
key = 5
low, high = 0, len(arr)-1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Element found at index", mid)
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Element not found")

