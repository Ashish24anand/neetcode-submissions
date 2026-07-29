class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = []
        res = 0
        for l in s:
            if l not in win:
                win.append(l)
                print(" addend win and res", win, res)
            else:
                if len(win) > res:
                    print("win and res", win, res, l)
                    res = len(win)
                win_len = len(win)
                ind = 0
                while ind < win_len:
                    l1 = win[0]
                    print(
                        "loop", l1, l, win[0]
                    )
                    if l1 == l:
                        del win[0]
                        break
                    del win[0]
                    ind += 1
                win.append(l)
        return max(res, len(win))
                
            

        