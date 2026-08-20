class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for hc in t:
            if hc in freq:
                freq[hc]-=1
                if freq[hc]<0:
                    return False
            else:
                return False
        return True
            