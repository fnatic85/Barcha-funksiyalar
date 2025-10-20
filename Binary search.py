def binary_search(arr, target):
    """
    Performs a binary search on a sorted array to find the target value.

    Args:
        arr: The sorted list or array to search within.
        target: The value to search for.

    Returns:
        The index of the target value if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target not found in the array

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_value_found = 11
target_value_not_found = 6

result_found = binary_search(my_list, target_value_found)
if result_found != -1:
    print(f"Element {target_value_found} found at index {result_found}")
else:
    print(f"Element {target_value_found} not found in the list")

result_not_found = binary_search(my_list, target_value_not_found)
if result_not_found != -1:
    print(f"Element {target_value_not_found} found at index {result_not_found}")
else:
    print(f"Element {target_value_not_found} not found in the list")