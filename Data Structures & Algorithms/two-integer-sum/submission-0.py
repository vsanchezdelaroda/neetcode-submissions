class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # nums[i] + nums[j] = target
        hash_ind = {}

        # We can populate a hash with number as key, idx as value
        for idx, num in enumerate(nums):
            hash_ind[num] = idx
        
        # Now, we reiterate checking if the complementary (target - num[i]) exists in hash_ind
        for idx, num in enumerate(nums):
            comp = target - num

            # We also need to check that is not the same element
            if comp in hash_ind and hash_ind[comp] != idx:
                return [idx, hash_ind[comp]]
        
        return []