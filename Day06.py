"""
	Q:
		Given a N*N matrix
		all rows are sorted, and all columns are sorted.
		find the Kth larget element of the matrix

	A:
		case 1) don't use heapq in python
			1. make a new 1d array and copy matrix to 1d array
			2. quick sort
			3. find Kth
		case 2) use heapq in python -> use nlargest
"""