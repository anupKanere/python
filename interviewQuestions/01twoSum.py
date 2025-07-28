def twoSum(nums , target):
    seen = {}
    for key , num in enumerate(nums):
        compliment = target - num
        if compliment in seen:
            return key , seen[compliment]
        seen[num] = key
    return None


def main():
    nums = [1,2,3,4,5,6,7,8,9]
    target = 9
    print(twoSum(nums , target))
    
if __name__ == "__main__":
    main()