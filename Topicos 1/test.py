from cesar import cifra_cesar
import unittest


class CesarTests(unittest.TestCase):
    # Testa letras minusculas
    def test_1(self):
        self.assertEqual(cifra_cesar(1, [2], ["abc"]), [False, [""]])

    # testa caracteres especiais
    def test_2(self):
        self.assertEqual(cifra_cesar(1, [10], ["!#@"]), [False, [""]])

    # testa números
    def test_3(self):
        self.assertEqual(cifra_cesar(1, [9], ["412"]), [False, [""]])

    # Testa entradas validas
    def test_4(self):
        self.assertEqual(
            cifra_cesar(
                6,
                [2, 10, 0, 25, 1, 4],
                [
                    "VQREQFGT",
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                    "TOPCODER",
                    "ZWBGLZ",
                    "DBNPCBQ",
                    "LIPPSASVPH",
                ],
            ),
            [
                True,
                [
                    "TOPCODER",
                    "QRSTUVWXYZABCDEFGHIJKLMNOP",
                    "TOPCODER",
                    "AXCHMA",
                    "CAMOBAP",
                    "HELLOWORLD",
                ],
            ],
        )

    # Testa entrada vazia
    def test5(self):
        self.assertEqual(cifra_cesar(0, [], []), [False, [""]])

    # Testa deslocamento(key) negativo
    def test6(self):
        self.assertEqual(cifra_cesar(1, [-1], ["A"]), [False, [""]])

    # Testa entradas maiores que a especificação
    def test7(self):
        self.assertEqual(cifra_cesar(1, [1], ["" * 100]), [False, [""]])


unittest.main()
