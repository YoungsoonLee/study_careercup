"""
Q:
	Giv you an array which has n integers, it has both negative and positive integers.
	Now you need sort this array in a secial way. After that, the negative integers should in the front, 
	and the positive integers should in the back. Also the relative position should not be changed.
	eg, -1 1 3 -2 2 ans: -1 -2 1 3 2
	eg, 1 -3 4 2 -4 5 ans: -3 -4 1 4 2 5
	eg, 1 -3 4 2 -4 0 ans: -3 -4 1 4 2 0
	eg, 1 -3 4 0 2 -4 ans: -3 -4 1 4 0 2
	O(n) time and O(1) space complexity is perfect
"""
import unittest


def rearrange(array):
    p = 0
    for i in range(0, len(array)):
        cur = array[p]
        if cur >= 0:
            array.append(cur)
            del array[p]
        else:
            p += 1
    return array


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange([-1, 1, 3, -2, 2]), [-1, -2, 1, 3, 2])
        self.assertEqual(rearrange([1, -3, 4, 2, -4, 5]), [-3, -4, 1, 4, 2, 5])
        self.assertEqual(rearrange([1, -3, 4, 2, -4, 0]), [-3, -4, 1, 4, 2, 0])
        self.assertEqual(rearrange([1, -3, 4, 0, 2, -4]), [-3, -4, 1, 4, 0, 2])
        self.assertEqual(
            rearrange([-1, 1, 3, -2, -5, 2]), [-1, -2, -5, 1, 3, 2])

if __name__ == "__main__":
    unittest.main()
