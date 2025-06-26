from typing import List
from datetime import datetime

def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swapped = True
        if not swapped:
            break
    return arr


arr = [5,6,9,7,8,3,1,2]
# arr = [1, 2, 3, 5, 6, 7, 8, 9]

start_time = datetime.now()
print(bubble_sort(arr))
end_time = datetime.now()
print(f"Total time taken : {end_time - start_time}")