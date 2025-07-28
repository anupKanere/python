
def check_duplicate(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def check_duplicate_shorter(nums):
    return len(nums) != len(set(nums))

def main():
    nums = [1,2,3,4,5,6,7,8,9,9]
    print(check_duplicate(nums))
    
if __name__ == "__main__":
    main()