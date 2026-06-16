class Solution(object):
    def isValid(self,s):
        dict={'}':'{',']':'[',')':'('}
        stack=[]

        for ch in s:
            if ch in dict:
                if not stack or stack.pop()!=dict[ch]:
                    return False
            else:
                stack.append(ch)
        
        return len(stack)==0


