def find_duplicate(nums):
    seen = set()
    duplicate = set()

    for num in nums:
        if num in seen:
            duplicate.add(num)
        else:
            seen.add(num)
    return list(duplicate)


nums = [1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9, 9]
print(find_duplicate(nums))


# using data frame
import pandas as pd
df = pd.DataFrame({"values": nums})
duplicate = df[df.duplicated('values' , keep=False)]['values'].unique().tolist()
print(duplicate)