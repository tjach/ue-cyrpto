import unittest

from src.CaesarCipher import CasearCipher


class CeasarCipherTest(unittest.TestCase):

    def test_init(self):
        cc = CasearCipher()
        self.assertIsInstance(cc, CasearCipher)

    def test_crypt_empty(self):
        cc = CasearCipher()
        with self.assertRaises(AssertionError):
            cc.crypt(cleartext='')

    def test_single_char_wht_good_key(self):
        cc = CasearCipher(key=1)
        self.assertEqual(cc.crypt('A'), 'B')

    def test_pythonic_crypt(self):
        cc = CasearCipher(key=1)
        self.assertEqual(cc.pythonic_crypt('a'), 'a')

