s = "abcd"
t = "abcde"


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        for element in s_sorted:
            if element in t_sorted:
                t_sorted.remove(element)

        return "".join(t_sorted)


solution = Solution()


result = solution.findTheDifference(s, t)
print(result)
