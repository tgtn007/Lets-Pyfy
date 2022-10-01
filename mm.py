
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i,elm in enumerate(nums):
	    if target-elm in nums[i+1:] :
            temp=nums[(i+1):]
		    return [i,temp.index(target-elm)+i]
		    breakn