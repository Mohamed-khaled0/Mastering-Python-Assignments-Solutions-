# 1

import unittest

class MyTestCases(unittest.TestCase):

    def test_value_in_list(self):
        self.assertIn(10, [5, 7, 8, 10])  # Test 1

    def test_type_of_value(self):
        self.assertIsInstance(10, int)  # Test 2

    def test_number_return_true(self):
        self.assertTrue(100)  # Test 3

    def test_empty_list_return_false(self):
        self.assertFalse(bool([]))  # Test 4

    def test_number_greater_than_90(self):
        self.assertGreaterEqual(100, 90)  # Test 5

if __name__ == '__main__':
    unittest.main()


print("-" *150)

# 2 



import random
import string

def generate_serial():
    chars = string.ascii_letters + string.digits  # حروف + أرقام
    part1 = ''.join(random.choices(chars, k=4))
    part2 = ''.join(random.choices(chars, k=4))
    part3 = ''.join(random.choices(chars, k=6))
    serial = f"{part1}-{part2}-{part3}"
    return serial

print(generate_serial())
