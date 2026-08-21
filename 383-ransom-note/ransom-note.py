class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1={}
        dic2={}
        for hc in magazine:
            dic2[hc]=dic2.get(hc,0)+1
        for ch in ransomNote:
            dic1[ch]=dic1.get(ch,0)+1
            if dic1[ch]>dic2.get(ch,0):
                return False
        return True
        
        