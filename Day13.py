"""
Recursive~!!!!!
Given a rod of length n inches and an array of prices that contains prices of all pieces of a size smaller than n. 
Determine the maximum value obtainable by cutting up the rod and selling the pieces. 

For example, if length of the rod is 8 and the values of different pieces are given as following, 
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)

For example, if you cut the rod by 1 inch, the rod will be 8 pieces. 
2 inch -> 4 pices, 3 inch -> 3 pieces, 4 inch -> 2 pieces...

// length | 1 2 3 4 5 6 7 8 
// --------------------------------------------
// price | 1 5 8 9 10 17 17 20
Say the input is:
var prices = [10, 5, 8, 9, 10, 17, 17, 20 ];
function getRodMaxVal( height, prices ) {
...
}

Tip:
These can be solved using three approaches.
1) Recursive approach:
	Try using the recursive approach first. At the beginning, 
	you start by the initial stick length, this will be getRodMaxVal( prices.length, prices ).

2) Top-down dynamic programming approach (memoization)
	Modify approach 1) by caching duplicate works to improve efficiency. The interface will now look like:
	function getRodMaxVal(height, prices, memo){
		...
	}
	memo holds the computed subproblems solution.
	TIPS: memo is an object.

3) Bottom-up dynamic programming approach
	With the iterative approach, solve the problem from the smallest size input, 0, 
	and build it up to N length. Use a table (array in this case) to help you in building up the solution.
"""

def getRodMaxVal(height, prices, memo):
	if memo is None:
		memo = {}
	maxVal = 0
	i = 0
	key = None
	remainHeight = None

	for _ in range(i,height):
		remainHeight = height-i-1;
		key = str(i)+'-'+ str(remainHeight);		
		if key not in memo:
			memo[key] = prices[i] + getRodMaxVal(remainHeight, prices,memo);

		maxVal = max(maxVal, memo[key]);
		i = i+1
	#print(memo)
	return maxVal;


if __name__ == '__main__':
	prices = [1, 5, 8, 9, 10, 17, 17, 20]
	print(getRodMaxVal(8, prices, None))