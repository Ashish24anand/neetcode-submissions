class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs =[]
        for first_ind in range(len(nums)):
            for ind in range(len(nums)):
                if first_ind != ind:
                    if nums[first_ind]+nums[ind] == target:
                        return [first_ind, ind]

        