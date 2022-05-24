from ast import arg
from http.client import ImproperConnectionState
from random import randint
import unittest
def bubble_sort ( A ) :
    # We go through the list as many times as there are elements
    for i in range ( len ( A ) ) :
        # We want the last pair of adjacent elements to be (n -2 , n - 1 )
        for j in range ( len ( A ) - 1 ) :
            if A [ j ] > A [ j + 1 ] :
                # Swap
                A [ j ] , A [ j + 1 ] = A [ j + 1 ] , A [ j ]
    return A

def generate_random_array(max_int = 1000, max_array_size = 10):
    array_size = randint(0, max_array_size)
    A = [randint(0, max_int) for _ in range(0, array_size)]
    return A

class UnitTest(unittest.TestCase):
    def test_bubble_sort(self):
        for _ in range(50):
            input_array = generate_random_array(10, 3)
            print('now tesing :: ', input_array)
            A = input_array.copy()
            A_sorted = bubble_sort(input_array)
            print('bubble sort result :: ', A_sorted)
            actual_result = sorted(A)
            print('actual result :: ', A_sorted)
            self.assertEqual(A_sorted, actual_result)
            print('Passed...')

if __name__ == '__main__':
    unittest.main()


