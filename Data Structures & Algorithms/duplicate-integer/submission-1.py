class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums=set()
        for num in nums:
            if num not in new_nums:
                new_nums.add(num)
            else:
                return True
        return False
            

        