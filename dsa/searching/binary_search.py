def binary_search(arr , key):
    left , right = 0 , len(arr) - 1
    
    while left <= right:
        mid = (right + left) // 2
        if mid == key:
            return mid
        if key > mid:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1
        
    

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20]
check_num =16


is_present = binary_search(arr, check_num)
print(f"The number {is_present} is present" if is_present != -1 else "NOT PRESENT")

