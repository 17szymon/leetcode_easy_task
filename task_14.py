from typing import List


strs1 = ["flower", "flow", "flight"]
strs = ["reflower", "flow", "flight"]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short_word = min(strs, key=len)
        output = []
        find_letetter_second = True
        if len(strs) == 1:
            return "".join(strs)

        for id_short, letter_short in enumerate(short_word):
            for word in strs:
                if word == short_word:
                    continue
                for id_word, letter_word in enumerate(word):
                    if letter_word == letter_short and id_short == id_word:
                        output.append(letter_short)
                        break

        seen_elements = set()
        repeated_elements = []

        for element in output:
            if element not in seen_elements:
                seen_elements.add(element)
            elif element not in repeated_elements:
                repeated_elements.append(element)

        return "".join(repeated_elements)


solution = Solution()

result = solution.longestCommonPrefix(strs)
print(result)
