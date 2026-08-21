class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freq1={}
        freq2={}
        for i in range(len(s)):
            ch=s[i]
            hc=t[i]
            if ch in freq1 and freq1[ch]!=hc:
                return False
            if hc in freq2 and freq2[hc]!=ch:
                return False
            freq1[ch]=hc
            freq2[hc]=ch
        return True