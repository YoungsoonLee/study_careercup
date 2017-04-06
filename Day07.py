"""
    Q
        Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
        Do not allocate extra space for another array, you must do this in place with constant memory.

        For example,
        Given input array nums = [1,1,2],

        Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

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
    
