x = -121


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = x[::-1]
        if x == y:
            return True
        else:
            return False


solution = Solution()

result = solution.isPalindrome(x)
print(result)
