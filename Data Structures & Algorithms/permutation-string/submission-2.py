class Solution:
    

    def checkInclusion(self, s1: str, s2: str) -> bool:
        def make_feq(s: srt) -> dict:
            res ={}
            for c in s:
                if c in res:
                    res[c] += 1
                else:
                    res[c] = 1
            return res
        win_size = len(s1)
        s1_feq_count = make_feq(s1)
        print("s1_feq_count", s1_feq_count)
        for l in range(len(s2)-win_size+1):
            r = l+win_size
            # prev_flag = True
            # nex_expected = None
            # len_str = 0
            # for c in s2[l:r]:
            #     len_str += 1
            #     print("c: ", c, nex_expected, s1.find(c))
            #     if c in s1:
            #         if nex_expected == None or nex_expected == c:
            #             ind = s1.find(c)
            #             nex_expected = s1[(ind+1)%len(s1)]
            #             if len_str == win_size:
            #                 return True
            #         else:
            #             break
            #     else:
            #         break
            sub_str = s2[l:r]
            sub_str_feq = make_feq(sub_str)
            print("sub_str_feq, ",sub_str_feq)
            if sub_str_feq == s1_feq_count:
                return True
            # for i in range(len(sub_str)):
            #     c = sub_str[i]
            #     if c in s1_feq_count and s1_feq_count[c] == sub_str_feq[c] and i == len(sub_str)-1:
            #         return True
            #     else:
            #         break
            
        return False



        