import unittest

def move_zeros_to_left(A):

    right_pointer = len(A) - 1
    left_pointer = len(A) - 1

    while left_pointer >= 0:
        if A[right_pointer] == 0:
            while A[left_pointer] ==0:
                left_pointer -=1
            if left_pointer >= 0:
                A[right_pointer] = A[left_pointer]
                A[left_pointer] = 0

        left_pointer -= 1
        right_pointer -= 1



    return A

class UnitTest(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(move_zeros_to_left([1, 2, 0, 3, 0, -5, 6, 0, 0, 3]), [0, 0, 0, 0, 1, 2, 3, -5, 6, 3])
        self.assertEqual(move_zeros_to_left([0, 0, 0, 1, 2, 0, 3, 0, -5, 6, 0, 0, 0, 0, 3]), [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, -5, 6, 3])


if __name__ == '__main__':
    unittest.main()



