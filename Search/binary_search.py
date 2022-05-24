import unittest

##### Code starts here #####

# Array A, search value T,
# A is sorted in ascending order
def binary_search(A, T):
    L = 0
    R = len(A)-1

    while L <= R:
        m = (L+R) // 2
        if A[m] < T:
            L = m+1
        elif A[m] > T:
            R = m-1
        else:
            return m
    return -1

##### Code ends here #####

class UnitTest(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search([], 3), -1)
        self.assertEqual(binary_search([1, 2], 3), -1)
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4], 1), 0)
        self.assertEqual(binary_search([1, 2, 3, 4], 4), 3)


if __name__ == '__main__':
    unittest.main()