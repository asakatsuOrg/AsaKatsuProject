def moveZeroes(nums):
    for i in range(nums.count(0)):
        nums.append(nums.pop(nums.index(0)))
    
print(moveZeroes([0,1,0,3,12]))