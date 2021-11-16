from unittest import TestCase
from prime_numbers_sen import prime_numbers_sen


class Test(TestCase):
    def test_prime_numbers_sen(self):
        test_data = [
            #[2, [2]],
            #[3, [2, 3]],
            [4, [2, 3]],
            #[5, [2, 3, 5]],
            #[10, [2, 3, 5, 7]],
            #[20, [2, 3, 5, 7, 11, 13, 17, 19]]
        ]
        for test in test_data:
            prims = prime_numbers_sen(test[0])
            TestCase.assertListEqual(self, prims, test[1])
