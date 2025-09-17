#move zeros to end
def moveZeroes(nums):
    n=len(nums)
    l=0
    for i in range(n):
        if nums[i]!=0:
            nums[l],nums[i]=nums[i],nums[l]
            l+=1
    return nums
            
nums=[0,1,0,3,12]
print(moveZeroes(nums))  # Output: [1, 3, 12, 0, 0]