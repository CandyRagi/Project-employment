class Solution(object):
    def lengthOfLastWord(self,s):
        trim=s.strip()
        array=s.split()
        return len(array[len(array)-1])

# Faster ??
class Solution(object):
    def lengthOfLastWord(self,s):
        array=s.split()

        for i in array:
            continue

        return len(i)
