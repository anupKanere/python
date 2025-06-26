"""
Compare each element with the all other elements and if found number less than current number then swap it
"""
from typing import List

def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

# Swap when a smaller element is found instead of selecting the minimum element first and swapping only once at the end of the pass.
def selection_sort_2(arr : List[int]) -> List[int]:
    len_arr = len(arr)
    for i in range(len_arr):
        min_index = i
        for j in range(i+1 , len_arr):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
    return arr


arr = [5,6,9,7,8,3,1,2]

print(selection_sort_2(arr))
