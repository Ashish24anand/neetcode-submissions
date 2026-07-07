class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {')':'(', '}': '{', ']' : '['}
        stack =[]
        for letter in s:
            if letter in openToClose.keys():
                if len(stack)==0 or openToClose[letter] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(letter)
        return True if len(stack) == 0 else False
        