import unittest

import bubble_sort


class TestBuscaBinaria(unittest.TestCase):
    #     def test_lista_pequena(self):
    #         print("Resultado deve voltar [1, 2, 4, 5]")
    #         # deve devolver
    #         # [1, 5, 4, 2]
    #         # [1, 4, 5, 2]
    #         # [1, 4, 2, 5]
    #         # [1, 2, 4, 5]

    #         result = bubble_sort.bubble_sort([5, 1, 4, 2])

    #         self.assertEqual(result, [1, 2, 4, 5])

    def test_lista_grande(self):
        print("Resultado deve voltar [0, 1, 2, 3, 4, 5]")
        # deve devolver
        # [1, 3, 5, 4, 2, 0]
        # [1, 3, 4, 5, 2, 0]
        # [1, 3, 4, 2, 5, 0]
        # [1, 3, 4, 2, 0, 5]
        # [1, 3, 2, 4, 0, 5]
        # [1, 3, 2, 0, 4, 5]
        # [1, 2, 3, 0, 4, 5]
        # [1, 2, 0, 3, 4, 5]
        # [1, 0, 2, 3, 4, 5]
        # [0, 1, 2, 3, 4, 5]

        result = bubble_sort.bubble_sort([5, 1, 3, 4, 2, 0])

        self.assertEqual(result, [0, 1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()


# O resultado dos testes com seu programa foi:

# ***** [0.6 pontos]: Verificando funcionamento do bubble sort - Falhou *****
# AssertionError: Expected [1, 5, 3, 4, 2, 0]
# [1, 3, 5, 4, 2, 0]
# [1, 3, 4, 5, 2, 0]
# [1, 3, 4, 2, 5, 0]
# [1, 3, 4, 2, 0, 5]
# [1, 3, 2, 4, 0, 5]
# [1, 3, 2, 0, 4, 5]
# [1, 2, 3, 0, 4, 5]
# [1, 2, 0, 3, 4, 5]
# [1, 0, 2, 3, 4, 5]
# [0, 1, 2, 3, 4, 5]
#  but got [1, 5, 3, 4, 2, 0]
# [0, 5, 3, 4, 2, 1]
# [0, 3, 5, 4, 2, 1]
# [0, 2, 5, 4, 3, 1]
# [0, 1, 5, 4, 3, 2]
# [0, 1, 4, 5, 3, 2]
# [0, 1, 3, 5, 4, 2]
# [0, 1, 2, 5, 4, 3]
# [0, 1, 2, 4, 5, 3]
# [0, 1, 2, 3, 5, 4]
# [0, 1, 2, 3, 4, 5]
