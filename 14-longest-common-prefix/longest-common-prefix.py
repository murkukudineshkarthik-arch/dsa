class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        emp=""
        strs.sort()
        if len(strs)==0:
            return emp
        left=strs[0]
        right=strs[-1]
        for i in range(min(len(left),len(right))):
            if left[i]==right[i]:
                emp+=left[i]
            else:
                break
        return emp 


        