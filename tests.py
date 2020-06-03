from scrabble_calc import *
from remove_duplicates import *
import unittest


class Tests(unittest.TestCase):
    def test_scrabble(self):
        self.assertEqual(word_calc('xylophone'), 24)
        self.assertEqual(word_calc('fun'), 6)
        self.assertNotEqual(word_calc('an'), 3)
        self.assertNotEqual(word_calc('e'), 2)

    def test_rm_duplicates(self):
        self.assertEqual(no_duplicates([1, 2, 1, 2, 1, 2]), [1, 2])
        self.assertEqual(no_duplicates(['hi', 'hi', 'a', 'b']), ['hi', 'a', 'b'])
        self.assertEqual(no_duplicates(['a', 2, 3, 3, 'a', 'b', 4]), ['a', 2, 3, 'b', 4])

if __name__ == '__main__':
    unittest.main()