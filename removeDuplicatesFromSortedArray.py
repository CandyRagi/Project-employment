class Solution(object):
    def removeDuplicates(self,nums):
        dict={}

        total=0

        for i in nums:
            if i in dict:
                continue
            else:
                nums[total]=i
                dict[i]=total
                total+=1
       
       return total
