import unittest

from src.pi import Pi


class PiTest(unittest.TestCase):

    def test_pi_with_one_decimal(self):
        pi_expected = 3.1
        pi_result = Pi.calcular_pi(1)
        self.assertEqual(pi_expected, pi_result)  # add assertion here

    def test_pi_with_two_decimal(self):
        pi_expected = 3.14
        pi_result = Pi.calcular_pi(2)
        self.assertEqual(pi_expected, pi_result)  # add assertion here

    def test_pi_with_three_decimal(self):
        pi_expected = 3.141
        pi_result = Pi.calcular_pi(3)
        self.assertEqual(pi_expected, pi_result)  # add assertion here

    def test_pi_with_four_decimal(self):
        pi_expected = 3.1415
        pi_result = Pi.calcular_pi(4)
        self.assertEqual(pi_expected, pi_result)  # add assertion here

    def test_pi_with_five_decimal(self):
        pi_expected = 3.14159
        pi_result = Pi.calcular_pi(5)
        self.assertEqual(pi_expected, pi_result)  # add assertion here

    def test_pi_with_six_decimal(self):
        pi_expected = 3.141592
        pi_result = Pi.calcular_pi(6)
        self.assertEqual(pi_expected, pi_result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
