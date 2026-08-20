class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq={}
        freq1={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for hc in t:
            freq1[hc]=freq1.get(hc,0)+1
        if freq!=freq1:
            return False
        return True
        