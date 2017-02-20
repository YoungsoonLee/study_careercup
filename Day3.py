"""
Q:
	Given an array of distinct integer values, count the number of pairs of integers that 
	have different K. for example, given the array [1, 7, 5, 9, 2, 12, 3] and the difference
	k =2. there are four pairs with differnce 2: (1, 3), (3, 5), (5, 7), (7, 9)

A:
	1. given array is not sorted ? -> correct
	2. result have sorted. not reverse. for example, (1,3) (3,1) -> x

	time complexity
	space complexity
"""

from collections import defaultdict

def getElementywithK(array, k=None):
	if k is None:
		raise str('need to k')
	else:
		# input to hase each array with value is plua 2
		dic = defaultdict()
		result = ''
		for item in array:
			if array.count(item+k) > 0:
				dic[item] = item+k
		#print(dic)
		# it's okay there is blow code or not				
		for key, value in dic.items():
			
			if array.index(value):
				result += '(%i , %i)' % (key, value)
		
		return result


if __name__ =="__main__":
	print(getElementywithK([1, 7, 5, 9, 2, 12, 3], 2))

