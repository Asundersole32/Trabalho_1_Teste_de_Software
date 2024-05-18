from cesar import cifra_cesar
import unittest


class CesarTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cifra_cesar(1, [2], ["abc"]), False)

    def test_2(self):
        self.assertEqual(cifra_cesar(1, [10], ["!#@"]), False)

    def test_3(self):
        self.assertEqual(cifra_cesar(1, [9], ["412"]), False)

    def test_4(self):
        self.assertEqual(cifra_cesar(6, [2, 10, 0, 25, 1, 4], ["VQREQFGT", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "TOPCODER",
                                                               "ZWBGLZ", "DBNPCBQ", "LIPPSASVPH"]), True)


unittest.main()
