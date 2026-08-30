class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        count=0
        max_count=0
        for num in seen:
            if num-1 not in seen:
                count=1
                curr=num
                while curr+1 in seen:
                    count+=1
                    curr+=1
                max_count=max(max_count,count)
        return max_count

        



        