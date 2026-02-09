def selection_sort(arr):
    """
    Sorts an array in ascending order using the selection sort algorithm.
    
    The algorithm works by repeatedly finding the minimum element from the 
    unsorted portion and placing it at the beginning of the sorted portion.
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        None (sorts the list in place)
        
    Time Complexity: O(n²) in all cases
    Space Complexity: O(1)
    
    Example:
        >>> data = [64, 25, 12, 22, 11]
        >>> selection_sort(data)
        >>> print(data)
        [11, 12, 22, 25, 64]
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n - 1):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

data = [64, 25, 12, 22, 11]
selection_sort(data)
print("Sorted array:", data)    