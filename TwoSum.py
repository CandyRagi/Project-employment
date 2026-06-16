class Solution(object):
    def twoSum(self,nums,target):
        dict={}
        for index,num in emumerate(nums):
            complement=target-num
            if complement in dict:
                return [dict[complement],index]

            dict[num]=index
