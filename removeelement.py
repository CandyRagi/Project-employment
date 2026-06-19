class Solution(object):
    def removeElement(self,nums,val):
        j=0

        for i in range (0,len(nums),1):
            if(nums[i]!=val):
                nums[j]=nums[i]
                j+=1
        
        return j

# Easier Way

class Solution(object):
    def removeElement(self,nums,val):
        while val in nums:
            nums.remove(val)
        return len(nums)
