"""
Q1: 
	Given 25 horses, find the best 3 horses with minumum number of races.
	each race can have only 5 horses. You don't have a timer.

	25마리의 말이 있다. 최소한의 경기로 최고의 말 3마리를 찾아라.
	각 레이스는 오로지 5마리만 가능. 당신은 타이머가 없다.

A1:
	let me explain in detail. 

	race1: a1 a2 a3 a4 a5, winner: a1 
	race2: b1 b2 b3 b4 b5, winner: b1 
	race3: c1 c2 c3 c4 c5, winner: c1 
	race4: d1 d2 d3 d4 d5, winner: d1 
	race5: e1 e2 e3 e4 e5, winner: e1 
	race6: a1 b1 c1 d1 e1, winner: a1 

	lets arrange horses of 6th race in their final standing. lets say a1>b1>c1>d1>e1 

	a1 has beaten winners of all group winners so he is the fastest. 
	d1 and e1 could not make to top 3 so how can any other horse of their initial group make to top 3 (since we already know d1 and e1 were winners of their groups)? so we reject 2 groups d1 and e1. and b1 c1 are sent back to their respective groups because they have chances to be amongst top 3. 

	our job is to find ONLY 2nd and 3rd fastest because we already have a1 as the fastest horse. so who all can be the candidate for those 2 positions? 
	a2 and a3 (2nd and 3rd in 1st group, they are top two) 
	b1 and b2 (1st and 2nd of 2nd group, they are top two) 
	c1 (why only one from this? because even the winner of this group which was c1, had 2 horses above him in 6th race. so it cant come 1st or 2nd ever so this group is candidate for 3rd place only) 
	rest 2 groups were already rejected (i described above why) 
"""

"""
Q2: 
	if [a1, a2, a3, ..., aN, b1, b2, b3 ..., bN] is given input change to
	[a1,b2,a2,b2....aNbN], solution should be in-palce
"""

# A2:
"""
def swap(array, n):
	temp = array[n-1]
	array[n-1] = array[n]
	array[n] = temp
	return array


def rearrange(array, n):
	pivot = int(len(array)/2)
	for i in range(0,len(array)):
	 	swap(array, pivot)

	print(array)

rearrange(['a1','a2','a3','a4','b1','b2','b3','b4'], 4)
"""


def gen_arr(size):
    arr = []
    for i in range(size):
        arr.append('a%s' % (i + 1))
    for i in range(size):
        arr.append('b%s' % (i + 1))
    return arr
size = 4
arr = gen_arr(size)

index = size
while index < len(arr):
        # print(index)
        # print(size)
    arr.insert(((index - size) * 2) + 1, arr[index])
    index += 1
    del arr[index]

# print(arr)
