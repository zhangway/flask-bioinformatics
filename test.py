import unittest

from app import translate


class AppTestCase(unittest.TestCase):

    def test_translate(self):

        input_seq = 'ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG'

        self.assertEqual(translate(input_seq), 'MAIVMGR')


if __name__ == '__main__':
    unittest.main()
