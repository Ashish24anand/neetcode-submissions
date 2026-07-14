class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers), 1):
        #         if numbers[i] + numbers[j] > target:
        #             break
        #         if numbers[i] + numbers[j] == target:
        #             return[i+1, j+1]
        r = len(numbers)-1
        l = 0
        while r > l:
            csum = numbers[r] + numbers[l]
            if csum > target:
                r = r -1
            elif csum < target:
                l = l+1
            else:
                return [l+1, r+1]

        