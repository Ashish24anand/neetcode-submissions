class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        num_set = set(nums)
        longest = 0
        for n in nums:
            if n-1 in nums:
                length =1
                print(length, longest, n)
                while (n+length) in num_set:
                    length += 1
                longest = max(length, longest) 
        return longest+1 
        