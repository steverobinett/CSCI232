def selection_sort_verbose(arr):
    """
    Selection sort with detailed output showing each step of the algorithm.
    Useful for educational purposes and debugging.
    
    Args:
        arr: List of comparable elements to sort
        
    Returns:
        Tuple of (sorted_array, comparisons, swaps)
    """
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    print(f"Starting array: {arr}")
    print("=" * 60)
    
    for i in range(n - 1):
        min_index = i
        print(f"\nPass {i + 1}:")
        print(f"  Searching for minimum in indices {i} to {n - 1}")
        
        # Find minimum in unsorted portion
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        
        print(f"  Minimum value: {arr[min_index]} at index {min_index}")
        
        # Perform swap if needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
            print(f"  ✓ Swapped indices {i} and {min_index}")
        else:
            print(f"  ✗ No swap needed (already in position)")
        
        print(f"  Array now: {arr}")
    
    print("=" * 60)
    print(f"\nFinal sorted array: {arr}")
    print(f"Total comparisons: {comparisons}")
    print(f"Total swaps: {swaps}")
    
    return arr, comparisons, swaps

data = [64, 25, 12, 22, 11]
selection_sort_verbose(data)    
print("Sorted array:", data)