arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20]
check_num =16


def linear_search(arr , key):
    for i , num in enumerate(arr):
        if num == key:
            return f"Element found at index {i}"
    return "Element not present in the array"


is_present = linear_search(arr , check_num);
print(is_present)