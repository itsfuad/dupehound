import os
import shutil
import tempfile
import unittest
from dupehound import duplicates, checksum


class DuplicateTests(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.root)

    def write(self, name, data):
        path = os.path.join(self.root, name)
        with open(path, 'wb') as f:
            f.write(data)
        return path

    def test_finds_equal_contents_only(self):
        a = self.write('a.txt', b'repeat')
        b = self.write('b.dat', b'repeat')
        self.write('c.dat', b'unique')
        groups = duplicates([self.root])
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]['files'], sorted([a, b]))

    def test_different_contents_same_size(self):
        self.write('a', b'ab')
        self.write('b', b'cd')
        self.assertEqual(duplicates([self.root]), [])

    def test_single_file(self):
        self.assertEqual(duplicates([self.write('a', b'x')]), [])


if __name__ == '__main__':
    unittest.main()
