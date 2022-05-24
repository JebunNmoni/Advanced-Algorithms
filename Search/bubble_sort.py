import unittest

##### Code starts here #####

def bubble_sort(A):
    # We go through the list as many times as there are elements
    for i in range(len(A)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(A) - 1):
            if A[j] > A[j+1]:
                # Swap
                A[j], A[j+1] = A[j+1], A[j]
    return A
    
##### Code ends here #####

class UnitTest(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([3, 4]), [3, 4])
        self.assertEqual(bubble_sort([1, 3, 4]), [1, 3, 4])
        self.assertEqual(bubble_sort([3, 4, 1]), [1, 3, 4])
        self.assertEqual(bubble_sort([3, 4, 2]), [2, 3, 4])
        self.assertEqual(bubble_sort([135604, 1000000, 45, 78435, 456219832, 2, 546]), [2, 45, 546, 78435, 135604, 1000000, 456219832])
        self.assertEqual(bubble_sort([1, 2, 2, 1, 0, 0, 15, 15]), [0, 0, 1, 1, 2, 2, 15, 15])
        self.assertEqual(bubble_sort([23, 7, 13, 5]), [5, 7, 13, 23])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1]), [1])


if __name__ == '__main__':
    unittest.main()