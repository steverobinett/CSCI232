def insertion_sort(arr):
    # Start from the second element
    for i in range(1, len(arr)):
        # Store current element
        key = arr[i]
        
        # Move elements greater than key one position right
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at its correct position
        arr[j + 1] = key
def main():
  theArray = [64,25,12,22,11]
  insertion_sort(theArray)
  print(theArray)

main()