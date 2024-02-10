str1 = "ABCABC"
str2 = "ABC"


str122 = "ABABAB"
str221 = "ABAB"
str1423 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2432 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
str14342 = "CXTXNCXTXNCXTXNCXTXNCXTXN"
str223423 = "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN"
str12 = "ABABABAB"
str22 = "ABAB"
str1 = "LEET"
str2 = "CODE"


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        output = []

        last: str = None
        x = zip(reversed(str1), reversed(str2))
        for char1, char2 in x:
            if char1 == last and len(output) != 1:
                break
            if char1 == char2:
                output.append(char1)
                last = output[0]

        output = reversed(output)
        return "".join(output)


solution = Solution()

result = solution.gcdOfStrings(str1, str2)
print(result)
