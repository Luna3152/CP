class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement_target = target - num

            if complement_target in seen:
                return [seen[complement_target], i]
            seen[num] = i


if __name__ == "__main__":
    import ast

    nums = ast.literal_eval(input("numsを入力: "))
    target = int(input("targetを入力: "))

    result = Solution().twoSum(nums, target)
    print(result)
