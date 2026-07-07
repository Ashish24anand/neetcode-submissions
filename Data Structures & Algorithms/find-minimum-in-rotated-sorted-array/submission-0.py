class Solution:
    def findMin(self, nums: List[int]) -> int:
        st =0
        end = len(nums)-1
        while end > st:
            center = st + (end-st) // 2
            if nums[center] < nums[end]:
                end = center
            else:
                st = center + 1
        return nums[st] 


        