import unittest

import busca_binaria


class TestBuscaBinaria(unittest.TestCase):

    def test_primeiro_numero_do_meio(self):
        print("Resultado deve voltar 1 e printar 1")
        # 1
        # deve devolver => 1
        result = busca_binaria.busca(['a', 'e', 'i'], 'e')
        print('result is', result)

        self.assertEqual(result, 1)

    def test_não_esta_na_lista(self):
        print("Resultado deve voltar False e printar 2 3 4")
        # 2
        # 3
        # 4
        # # deve devolver => False
        result = busca_binaria.busca([1, 2, 3, 4, 5], 6)
        print('result is', result)

        self.assertEqual(result, False)

    def test_numero_lugar_Aleatorio(self):
        print("Resultado deve voltar 3 e printar 2 4 3")
        # 2
        # 4
        # 3
        # deve devolver => 3
        result = busca_binaria.busca([1, 2, 3, 4, 5, 6], 4)
        print('result is', result)

        self.assertEqual(result, 3)

    def test_lista_apenas_um_numero(self):
        print("Resultado deve voltar False e printar 7")
        # 7
        # deve devolver => False
        result = busca_binaria.busca([7], 1)
        print('result is', result)

        self.assertEqual(result, False)

    def test_lista_varios_numero(self):
        print("Resultado deve voltar False e printar ?")
        # 7
        # deve devolver => False
        result = busca_binaria.busca(
            [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 15)
        print('result is', result)

        self.assertEqual(result, False)

    def test_altura(self):
        print("test_altura")

        lista = list(range(0, 80))
        result = busca_binaria.busca(
            lista, 36)
        print('result is', result)

        self.assertEqual(result, 36)

    def test_largura(self):
        print("test_largura")

        lista = list(range(0, 25))
        result = busca_binaria.busca(
            lista, 24)

        self.assertEqual(result, 24)


if __name__ == '__main__':
    unittest.main()


# ***** [0.6 pontos]: Verificando funcionamento da busca binária (lista: [1, 2, 3, 4, 5], buscando: 6, retorno: False, imprima: 2 3 4 ) - Falhou *****
# AssertionError: Expected 2
# 3
# 4
#  but got --------------
# 2
# 3
# 4


# ***** [0.6 pontos]: Verificando funcionamento da busca binária (lista: [1, 2, 3, 4, 5, 6], buscando: 4, retorno: 3, imprima: 2 4 3 ) - Falhou *****
# AssertionError: Expected 2
# 4
# 3
#  but got --------------
# 2
# 4
# 3
