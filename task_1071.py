str16 = "ABCABC"
str26 = "ABC"


str1 = "ABABAB"
str2 = "ABAB"
str31 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str22 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
str14342 = "CXTXNCXTXNCXTXNCXTXNCXTXN"
str223423 = "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN"
str12 = "ABABABAB"
str22 = "ABAB"
str12 = "LEET"
str22 = "CODE"
str1 = "EFGABC"
str2 = "ABC"


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        output = []
        first = None
        x = zip(reversed(str1), reversed(str2))
        for char1, char2 in x:
            if char1 != char2:
                return ""

        new_str = str1.replace(str2, "")
        if len(new_str) == 0:
            return str2
        else:
            for i in new_str:
                if len(output) > 1 and i == first:
                    return "".join(output)
                output.append(i)
                first = output[0]
            return "".join(output)


solution = Solution()

result = solution.gcdOfStrings(str1, str2)
print(result)
