class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(len(nums)-1):
            res.append(res[i]*nums[i])
        # print("res", res)
        post = 1
        for j in range(len(nums)-1, -1, -1):
            # print("j",j, post)
            res[j] = res[j] * post
            post = post * nums[j]
        return res
        