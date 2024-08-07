import unittest

def sumar(*args):
    suma = 0
    for n in args:
        suma += n
    return suma


# Clase de prueba
class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(1, 5), 6)  # Prueba básica
        self.assertEqual(sumar(-5, 1), -4)  # Prueba con números negativos y positivos
        self.assertEqual(sumar(0, 0), 0)  # Prueba con ceros
        self.assertEqual(sumar(-5, -5), -10)  # Prueba con números negativos
        self.assertEqual(sumar(5000, 4000), 9000)  # Prueba con números grandes

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()

