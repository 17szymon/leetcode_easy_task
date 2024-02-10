str81 = "ABCABC"
str28 = "ABC"


str122 = "ABABAB"
str221 = "ABAB"
str1234 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2324 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
str1 = "CXTXNCXTXNCXTXNCXTXNCXTXN"
str2 = "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN"


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        output = []
        id = 0
        lst_id = 0
        first: str = None
        x = zip(reversed(str1), reversed(str2))
        for char1, char2 in x:
            if char1 == char2:
                if char1 in output and char1 != first:
                    id += 1
                    continue
                elif id != lst_id:
                    break

                else:
                    output.append(char1)
                    first = output[-1]
                    id += 1
                    lst_id = id

        output = reversed(output)
        return "".join(output)


solution = Solution()

result = solution.gcdOfStrings(str1, str2)
print(result)
