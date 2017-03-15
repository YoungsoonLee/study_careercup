"""
	Q:
		Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. 
		Find this single element that appears only once.

		ex1.
			Input: [1,1,2,3,3,4,4,8,8]
			Output: 2
		ex2.
			Input: [3,3,7,7,10,11,11]
			Output: 10

		Your solution should run in O(log n) time and O(1) space.
"""




"""
#  this is not answer because not O(log n)
def findOneElement(array):
	for item in array:
		if array.count(item) == 1:
			return item

# use even and odd
def findOneEl(nums):	
	if not nums:
		return 0

	low = 0
	high = len(nums)
	while(low<=high):
		mid = low + int((high-low)/2)
		print(mid, len(nums), high, low)

		if mid == len(nums) -1:
			return nums[-1]

		if (nums[mid] == nums[mid-1]) and ( len(nums[0:mid+1])%2 == 0 ) :
			low = mid+1
		elif (nums[mid] == nums[mid+1]) and (len(nums[mid:-1]) %2 == 0):
			low = mid+1
		else:
			high = mid -1
	return nums[low]



def findOneElementByBinarySearch(array):
	 return dfs(array,0,len(array)-1)

def dfs(nums,start,end):
        if start==end:
            return nums[start]
        n=len(nums)
        m=int((start+end)/2)
        l=int((end-start)/2)
        r=int((end-start)/2)

        print(m,l,r)

        if nums[m]==nums[m+1]:
            r+=1
        elif nums[m]==nums[m-1]:
            l+=1
        else:
            return nums[m]
        print(l%2, l, r, start, end)
        if l%2==0:
            return dfs(nums,end-r+1,end)
        else:
            return dfs(nums,start,start+l-1)
"""


if __name__ == '__main__':
	a = [1,1,2,3,3,4,4,8,8]
	print(findOneEl(a))
	b = [3,3,7,7,10,11,11]
	print(findOneEl(b))

