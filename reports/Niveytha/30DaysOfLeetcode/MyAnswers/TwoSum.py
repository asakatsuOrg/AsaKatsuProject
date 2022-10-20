def twoSum(nums, target):
    # !Solution 1
    # for x in range(len(nums)):
    #     diff = target - nums[x]
    #     if diff in nums and nums.index(diff) != x:
    #         return [x, nums.index(diff)]
    # return -1

    # !Solution 2 - Best
    diffDict = {}   # <diff, index>
    for x in range(len(nums)):
        diff = target - nums[x]
        if nums[x] in diffDict:
            return [diffDict[nums[x]], x]
        diffDict[diff] = x

print(twoSum([3, 2, 4], 6))