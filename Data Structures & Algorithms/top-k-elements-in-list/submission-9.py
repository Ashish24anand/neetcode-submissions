class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ks = []
        number_counts = {}
        for n in nums:
             number_counts[n] = 1 +  number_counts.get(n, 0)
        res_arr = [0]*len(nums)
        res_dict = {}
        # print("number_counts", number_counts)
        for key, val in number_counts.items():
            if len(res_dict.keys()) < k:
                res_dict[key] = val
                continue
            min_key = None
            for rd in res_dict.keys():
                if res_dict[rd] < val:
                    if min_key == None:
                        min_key = rd
                    elif res_dict[min_key] >  res_dict[rd]:
                        min_key = rd
                    # print("res_dict", res_dict, rd, val)
            if min_key != None:
                res_dict[key] = val
                res_dict.pop(min_key)
                # break
        return list(res_dict.keys())
                
        #     # print(key, val)
        #     for lr in ks_count:
        #         if val > lr
        #     res_arr[val-1] = key
        # res =[]
        # print("res_arr", res_arr)
        # # for i in range(len(res_arr)-1, 0, -1):
        # i = len(res_arr)-1
        # while i>=0:
        #     print("res", res)
        #     if res_arr[i] == 0:
        #         i -= 1
        #         continue
        #     res.append(res_arr[i])
        #     if len(res) == k:
        #         return res
        #     i -= 1

