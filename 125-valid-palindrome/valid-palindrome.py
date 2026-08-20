class Solution:
    def isPalindrome(self, s: str) -> bool:
        emp=""
        for ch in s:
            if ch.isalnum():
                emp+=ch.lower()
        left=0
        right=len(emp)-1
        while left<right:
            if emp[left]!=emp[right]:
                return False
            else:
                left+=1
                right-=1
        return True        


        