from nums9 import nums9

nums1 = [1, 2, 2, 4]  # [2,3]
nums2 = [1, 1]  # [1,2]
nums3 = [2, 2]  # [2,1]
nums4 = [3, 2, 2]  # [2,1]
nums5 = [2, 3, 2]  # [2,1]
nums6 = [3, 2, 3, 4, 6, 5]  # [3,1]
nums7 = [3, 3, 1]  # [3,2]
nums8 = [1, 5, 3, 2, 2, 7, 6, 4, 8, 9]  # [2,10]


class Solution:
    def findErrorNums(self, nums):
        nums_set = set(nums)
        for element in range(1, len(nums) + 1):
            if element not in nums_set:
                missing_element = element

        for element in nums_set:
            if element in nums:
                nums.remove(element)
        nums.append(missing_element)
        return nums


nums = [nums1, nums2, nums3, nums4, nums5, nums6, nums7, nums8, list(nums9)]

solution = Solution()

for num in nums:
    result = solution.findErrorNums(num)
    print(result)
