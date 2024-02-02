s = "b"
t = "abc"


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        elif len(s) == 1:
            if s in t:
                return True
            else:
                return False

        s = list(s)
        for i in range(len(t)):
            if t[i] == s[0]:
                s.remove(s[0])
            if len(s) == 0:
                break

        if len(s) == 0:
            return True
        else:
            return False


solution = Solution()


result = solution.isSubsequence(s, t)
print(result)
