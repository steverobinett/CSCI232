def insertion_sort_verbose(arr):
    print(f"Initial array: {arr}")
    print()
    
    for i in range(1, len(arr)):
        key = arr[i]
        print(f"Pass {i}: Inserting {key}")
        
        j = i - 1
        while j >= 0 and arr[j] > key:
            print(f"  Shifting {arr[j]} to the right")
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        print(f"  Array after pass {i}: {arr}")
        print()
    
    print(f"Final sorted array: {arr}")

def main():
  theArray = [64,25,12,22,11]
  insertion_sort_verbose(theArray)
  print(theArray)

main()