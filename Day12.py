"""
Given an input string and ordering string, need to return true if the
ordering string is present in input string

example
	input = "hello world!"
	ordering = "hlo!"
	result = False (all Ls are not before all Os)

	input = "hello world!"
	ordering = "!od"
	result = False (the input has '!' coming after 'o' and after 'o' but the pattern needs it to come before 'o' and 'd')

	input = "hello world!"
	ordering = "he!"
	result = True

	input = "aaaabbbcccc"
	ordering = "ac"
	result = True
"""

def checkPresentOrdering(input, ordering):
	# if input length less than 2, just return True
	if len(input) < 1:
		return 'need input'

	# if ordering 
	if len(ordering) < 1:
		return 'need ordering'

	dic = {}
	i = 0

	for _ in range(0,len(input)):
		if input[i] in dic:
			dic[input[i]].append(i)
		else:
			dic[input[i]] = [i]
		i = i+1

	# use max number
	# min(s), max(s) : O(n)
	i = 0
	result = True
	for _ in range(0,len(ordering)-1):
		# print(p, c, max(dic[p]), max(dic[c]))
		if max(dic[ordering[i]]) > max(dic[ordering[i+1]]):
			result = False
		else: 
			i = i+1

	return result

	# use last value


if __name__ == "__main__":
	input = "hello world!"
	ordering = "hlo!"
	print(checkPresentOrdering(input, ordering))

	input = "hello world!"
	ordering = "!od"
	print(checkPresentOrdering(input, ordering))

	input = "hello world!"
	ordering = "he!"
	print(checkPresentOrdering(input, ordering))

	input = "aaaabbbcccc"
	ordering = "ac"
	print(checkPresentOrdering(input, ordering))