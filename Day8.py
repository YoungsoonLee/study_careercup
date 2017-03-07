"""
	Q:
		Given an array and a value, remove all instances of that value in place and return the new length.
		Do not allocate extra space for another array, you must do this in place with constant memory.
		The order of elements can be changed. It doesn't matter what you leave beyond the new length.

		Example:
		Given input array nums = [3,2,2,3], val = 3

		Your function should return length = 2, with the first two elements of nums being 2.
"""

""" 
	use python function 
	Time Complexity : O(N^2)
		python list index: O(1)
		python list del or remove: O(N)
"""
def removeElement(nums, val):
	"""
	:type nums: List[int]
	:type val: int
	:rtype: int
	"""
	try:
		while nums.index(val) is not None:
		    del nums[nums.index(val)]
		return len(nums)
	except Exception as e:
		return len(nums)

"""
	use python function  
	Time Complexity : O(N)
		python count: O(N)
		python list index: O(1)
"""
def removeElement_firstSort(nums, val):
	# nums.sort()
	for i in range(0, nums.count(val)):
		j = nums.index(val)
		if j == 0:
			nums = nums[j+1:]
		else:
			nums = nums[0:j] + nums[j+1:]
	print(nums)
	#print(len(nums))


def removeElement2(nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i


if __name__ == "__main__":
    #a = [3, 2, 2, 3]
    #a = [3, 2, 2, 3,4,4,5]
    #val = 3
    a = [4, 5]
    val = 4
    # print(s.removeElement(a, val))
    #removeElement_firstSort(a, val)
    print(removeElement2(a, val))
