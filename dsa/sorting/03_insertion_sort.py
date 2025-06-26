from typing import List

def insertion_sort(arr:List[int]) -> List[int]:
    n = len(arr)
    for i in range(1 , n - 1):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    
    return arr
        
arr = [7, 3, 5, 1, 9]
sorted = insertion_sort(arr)
print(f"SORTED ARRAY : {sorted}")