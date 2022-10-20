def intersection(nums1, nums2):
    # !Solution 1
    # nums1, nums2 = set(nums1), set(nums2)
    # res = []
    # for num in nums1:
    #     if num in nums2:
    #         res.append(num)
    # return res

    # !Solution 1
    return list(set(nums1) & set(nums2))

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection(nums1, nums2))