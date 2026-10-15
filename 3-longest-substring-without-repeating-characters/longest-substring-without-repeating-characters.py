class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left=0
        temp=0
        ans=0
        seen=set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[left])
                left+=1
            
            seen.add(s[r])
            ans=max(ans,r-left+1)
        return ans        

        