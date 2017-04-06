"""
	Q:
		Given an int array which might contain duplicates, find the largest 
		subset of it which form a sequence
		ex, [1,6,10,4,7,9,5] -> 4,5,6,7

		sorting is an obvious solution. can this be O(n)?

	todo: need to check largest subset sequence
	
"""
from collections import defaultdict

def findLargestSubset(array):
	# s1. sort
	# how about using dic -> use sapce
	# use array.sort() -> how to remove dup	
	array.sort()
	#print(array)
	result = index = [0, 0] # save start index and end index for search sequence
	for i in range(1, len(array)):
		prev = array[i-1]
		cur = array[i]
		# next = array[i+1]
		print(i, prev, cur)
		if i == 1: #first
			if(cur-prev) == 1:
				index[0] = i-1
				#if(next-cur) == 1:
				#	pass
		else:
			if(cur-prev) == 1:
				if index[0] != 0: # end index
					index[1] = i
				else:
					index[0] = i-1
			else:
				#if (cur - prev) > 1: 
					#print(i, len(array)-1)
				if (cur - prev) > 1:  ## count
					result = index.copy()
					index =[0, 0] # reset

		print(index)
		print(result)
		print('='*50)
	if index[0] !=0:
		result = index.copy()
	print(array[result[0]:result[1]+1])
	#print(index)

	# s2. find sequence

def find(arr):
    table = {}
    first = 0
    last = 0
    for i in arr:
        beg = end = i
        if i in table:
            continue
        table[i] = 'EXISTED'
        if i - 1 in table:
            beg = table[i-1]
        if i + 1 in table:
            end = table[i+1]
        table[beg] = end
        table[end] = beg
        if end - beg > last - first:
            first = beg
            last = end
    return list(range(first, last + 1))

if __name__ == '__main__':
	a = [1,6,10,4,7,9,5]
	b = [1,10,5,3,4,7,9,8,11,12,13,15,17]
	c = [1,2,4,5,6,9,8,11,12,13,15,17]
	d = [1,2,3,4,5,9,8,11,12,13,14,15]
	#findLargestSubset(a)
	#findLargestSubset(b)
	#findLargestSubset(c)
	#findLargestSubset(d)
	
	print(find(a))
	print(find(b))
	print(find(c))
	print(find(d))
	#findLargestSubset(d)
	