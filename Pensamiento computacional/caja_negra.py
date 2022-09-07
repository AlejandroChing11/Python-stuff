import unittest


def suma(num_1, num_2):
    return abs(num_1) + num_2


class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)

    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)


if __name__ == '__main__':
    unittest.main()



#Las pruebas de caja negra lo que hacen es hacer test por funicon, comprobando si es verdadero el resultado esperado, por tal razón se deben utilizar 2 variables como lo son, suma y resultado
#en este caro suma es la funcion y resultado es lo que esperamos de 'suma'.
