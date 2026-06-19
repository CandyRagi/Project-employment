class Solution(object):
    def strStr(self,haystack,needle):
        for i in range(0,len(haystack)-len(needle)+1,1):
            if(haystack[i]==needle[0]):
                if(haystack[i:i+len(needle)]==needle):
                    return i
        
        return -1


# Better Solution 
class Solution(object):
    def strStr(self,hatstack,needle):
        return haystack.find(needle)
