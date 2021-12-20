import unittest

import busca_binaria


class TestBuscaBinaria(unittest.TestCase):
    def test_primeiro_numero_do_meio(self):
        print("Resultado deve voltar 1 e printar 1")
        # 1
        # deve devolver => 1
        result = busca_binaria.busca(['a', 'e', 'i'], 'e')

        self.assertEqual(result, 1)

    def test_não_esta_na_lista(self):
        print("Resultado deve voltar False e printar 2 3 4")
        # 2
        # 3
        # 4
        # # deve devolver => False
        result = busca_binaria.busca([1, 2, 3, 4, 5], 6)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()

# print(busca([1, 2, 3, 4, 5], 6))
# 2
# 3
# 4
# # deve devolver => False
# print('aaaaaaaaa')
# print(busca([1, 2, 3, 4, 5, 6], 4))
# 2
# 4
# 3
# deve devolver => 3
