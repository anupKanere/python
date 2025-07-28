def merge_array(nums1, nums2):
    merged = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    return merged


nums1 = [1, 3, 5, 7, 9]
nums2 = [2, 4, 6, 8]

print(merge_array(nums1, nums2))
