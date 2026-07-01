class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=1
        l=len(nums)
        while i<l:
            while j<l:
                if nums[i]+nums[j]==(target) and i!=j:
                    return [i,j]
                    break
                else:
                    j+=1
            i=i+1
            j=2
          
            
