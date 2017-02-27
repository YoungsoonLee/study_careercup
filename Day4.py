"""
	Q:
		Eaxmple, Print all positive integer solutions to the equation a^3 + b^3 = c^3+d^3 
		where a,b,c and d are integers between 1 and 1000

	A:
		time complexity
		space complexity
"""
from collections import defaultdict

def n3solution(n=None):
	if n is None:
		n = 10
	dic = defaultdict()
	
	for c in range(1, n):
		for d in range(1, n):
			result = pow(c, 3)+pow(d, 3)
			dic[result] = [c, d]
			# print(c,d, result)
	# print(dic)
	for result, value in dic.items():
		print('(%i, %i) = (%i, %i) , result: %i' %(value[0],value[1],value[0],value[1],result))


if __name__ == "__main__":
	n3solution()
