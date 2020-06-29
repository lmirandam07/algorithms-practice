class Solution:
    def singleNumber(self, nums) -> int:
        single = set()
        for num in nums:
            if num in single:
                single.remove(num)
            else:
                single.add(num)
        return single.pop()
