"""
	Q:
		Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
		For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

		Note:
			You must do this in-place without making a copy of the array.
			Minimize the total number of operations.
"""

"""
	count: O(N)
	index: O(1)
	append: O(1)

	Total Time Complexity: O(N)
"""


def rearrangeZero(array):
    c = array.count(0)
    for _ in range(0, c):
        i = array.index(0)
        if i == 0:
            array = array[i + 1:]
        else:
            array = array[:i] + array[i + 1:]
        array.append(0)

    return array


"""
	use from collections import Counter
	Counter: O(NLogN)
	index: O(1)
	append: O(1)

	Total Time Complexity: O(NLogN)
"""
from collections import Counter


def rearrangeZero2(array):
    c = Counter(array)
    c = c[0]
    # print(c)
    for _ in range(0, c):
        i = array.index(0)
        if i == 0:
            array = array[i + 1:]
        else:
            array = array[:i] + array[i + 1:]
        # array.append(0)
    print(array == array)
    return array

# in-place


def moveZeroes(nums):
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
        # print(nums)
    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    # print(rearrangeZero(nums))
    # print(rearrangeZero2(nums))
    print(moveZeroes(nums))
