
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    if len(nums) == 0:
        return count
    else:
        for j in range(1, len(nums)):
            if nums[count] != nums[j]:
            	count += 1
            	nums[count] = nums[j]
        return count+1



if __name__ == "__main__":
	print(removeDuplicates([1,1,2]))
	print(removeDuplicates([1,1,2,2,3,3,4]))
	print(removeDuplicates([1,1,2,2,3,3,4,5,6,6]))