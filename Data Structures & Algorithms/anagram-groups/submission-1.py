class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        substr = []
        carcounters = {}
        def checkchar(a,b):
            if a == b:
                return True
            else:
                return False
        def carcounter(a):
            cc = {}
            for c in a:
                if c in cc:
                    cc[c] += 1
                else:
                    cc[c] = 1
            return cc


        for m in range(len(strs)):
            # print("m", m)
            carcounters[strs[m]] = carcounter(strs[m])
            if m == 0:
                substr.append([strs[m]])
                continue
            isadded = False
            # print("substr", substr)
            for  i in range(len(substr)):
                # print(len(substr[i][0]) , len(strs[m]))
                if len(substr[i][0]) != len(strs[m]):
                    continue
                # print("a, b",substr[i][0], strs[m], checkchar(substr[i][0], strs[m]))
                if checkchar(carcounters[substr[i][0]], carcounters[strs[m]]):
                    substr[i].append(strs[m])
                    isadded = True
                    break
            if not isadded:
                substr.append([strs[m]])
        # print(substr)
        return(substr)

        