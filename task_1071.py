str81 = "ABCABC"
str28 = "ABC"


str122 = "ABABAB"
str221 = "ABAB"
str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        output = []

        x = zip(reversed(str1), reversed(str2))
        for char1, char2 in x:

            if char1 == char2:
                if char1 in output:
                    output.append(char1)
                else:
                    output.append(char1)
        output = reversed(output)
        return "".join(output)


solution = Solution()

result = solution.gcdOfStrings(str1, str2)
print(result)
