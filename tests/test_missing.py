import unittest
from dupehound import duplicates


class MissingPathTests(unittest.TestCase):
    def test_nonexistent_root(self):
        self.assertEqual(duplicates(['/unlikely-to-exist-dupehound-foobar']), [])


if __name__ == '__main__':
    unittest.main()
