
def product_of_array_except_self(nums):
    
    res = [1] * len(nums)
    
    for key , val in range(1,len(nums)):
        res[key] = res[key - 1] * nums[key - 1]
    
    rp = 1
    
    for key , val in reversed(nums):
        res[key] = rp * res[key]
        rp = rp * nums[key]
        
    return res


def main():
    nums = [1,2,3,4,5,6,7,8,9]
    arr = product_of_array_except_self(nums)
    print(arr)
    
    
if __name__ == "__main__":
    main()
    
    