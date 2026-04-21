class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                    break


if __name__ == "__main__":
    import ast

    nums = ast.literal_eval(input("numsを入力: "))
    target = int(input("targetを入力: "))

    result = Solution().twoSum(nums, target)
    print(result)
