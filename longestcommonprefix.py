class Solution(object):
    def longestCommonPrefix(self,strs):
        strs.sort()

        first=strs[0]
        last=strs[-1]
        prefix=""

        for i in range (min(len(first,last))):
            if(first[i]==last[i]):
                prefix+=first[i]
            else:
                return prefix

        return prefix
