class Solution:
    def reverseString(self, s: List[str]) -> None:
        l=len(s)-1
        i=0
        while(i<l):
            s[i],s[l]=s[l],s[i]
            i=i+1
            l=l-1
        