from typing import List


strs = ["flower", "flow", "flight"]
strs2 = ["reflower", "flow", "flight"]
strs3 = ["ab", "a"]
strs34 = ["cir", "car"]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        list_words = []
        output = []
        for word in strs:
            list_words.append(list(word))

        zipped_elements = zip(*list_words)

        for elements in zipped_elements:
            if len(set(elements)) == 1:
                output.append(elements[0])
            else:
                break

        return "".join(output)


solution = Solution()

result = solution.longestCommonPrefix(strs)
print(result)
