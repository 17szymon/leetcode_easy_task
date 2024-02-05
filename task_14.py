from typing import List


strs1 = ["flower", "flow", "flight"]
strs = ["cir", "car"]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short_word = min(strs, key=len)
        output = []
        if len(strs) == 1:
            return "".join(strs)

        for letter_short in short_word:

            for word in strs:

                if word == short_word:
                    continue
                for letter_word in word:

                    if letter_short in word:
                        find_letetter = True
                        continue
                    else:
                        find_letetter = False
                        continue
                if letter_word == letter_short:
                    find_letetter = False

            if find_letetter == True:
                output.append(letter_short)
        if output is []:
            return ""
        else:
            return "".join(output)


solution = Solution()

result = solution.longestCommonPrefix(strs)
print(result)
