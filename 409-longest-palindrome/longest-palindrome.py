class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        length=0
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for values in freq.values():
            if values%2==0:
                length+=values
            else:
                length+=values-1
        for val in freq.values():
            if val%2!=0:
                length+=1
                break
        return length   

            
            
            

        