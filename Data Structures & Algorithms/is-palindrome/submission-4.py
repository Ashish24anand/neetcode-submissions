class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s)-1
        l = 0
        while r>l:
            print(s[l], s[r])
            if not s[r].isalnum():
                print("right", s[r])
                r -= 1
                continue
            if not s[l].isalnum():
                l += 1
                continue
            if s[r].lower() == s[l].lower():
                print(s[l], s[r], "false")
                r -= 1
                l += 1
                continue
            else:
                
                return False
        return True
        