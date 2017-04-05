"""
	Q:
		Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
		n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
		Find two lines, which together with x-axis forms a container, such that the container contains the most water.

		Note: You may not slant the container and n is at least 2.
"""
def findLines(n_array):
	mid = n_array[int( len(n_array) / 2 )-1]
	line_1 = ()
	line_2 = ()
	for i in range(0, len(n_array)):
		if i <= mid:
			line_1 = (n_array[i], len(n_array))
			line_2 = (len(n_array), n_array[i])
		else:
			line_1 = (0, len(n_array))
			line_2 = (len(n_array), i)
		print(i, line_1, line_2)


if __name__ == '__main__':
	a = [1,2,3,4]
	findLines(a)

