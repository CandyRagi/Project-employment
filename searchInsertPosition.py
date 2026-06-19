# log (n)

class Solution(object):
    def searchInsert(self,nums,target):
        start=0
        last=len(nums)-1

        if(nums[start]==target):
            return start
        if(nums[last]==target):
            return last
        
        while start<=last:
            mid=(start+last)//2

            if(nums[mid]==target):
                return mid
            if(target>nums[mid]):
                start=mid+1
            else:
                last=mid-1

        
        return start

# (n)
class Solution(object):
    def searchInsert(self,nums,target):
        for i in range(len(nums)):
            if(nums[i]>=target)
                return i
        return len(nums)    

