class Solution(object):
    def mySqrt(self,x):
        if(x<2):
            return x
        left,right=2,x//2

        while(right>=left):
            mid=(left+right)//2
            s=mid*mid

            if(s>x):
                right=mid-1
            elif(s<x):
                left=mid+1
            else:
                return mid

        return right

