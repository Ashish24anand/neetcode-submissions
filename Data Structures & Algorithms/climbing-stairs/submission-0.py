class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        st_arr = [1]

        for i in range(n):
            # if i == n-1:
            #     print(st_arr)
            #     return st_arr[-1]
            if len(st_arr)>1:
                value = st_arr[-1]+ st_arr[-2]
            else:
                value = st_arr[-1]

            st_arr.append(value)
        return st_arr[-1]


        