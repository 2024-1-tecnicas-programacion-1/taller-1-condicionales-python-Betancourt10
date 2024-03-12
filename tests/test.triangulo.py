import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.triangulo import evaluar

class TestTriangulo(unittest.TestCase):
    def test_no_es_un_triangulo_valido(self):
        valor_esperado = "No es un triángulo válido."
        valor_actual = evaluar(3.9, 6.0, 1.2)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_es_un_triangulo_equilatero(self):
        valor_esperado = "Es un triángulo equilátero."
        valor_actual = evaluar(3, 3, 3)
        self.assertEqual(valor_esperado, valor_actual) 

    def test_es_un_triangulo_isosceles(self):
        valor_esperado = "Es un triángulo isósceles."
        valor_actual = evaluar(5, 8, 5)
        self.assertEqual(valor_esperado, valor_actual) 

    def test_es_un_triangulo_escaleno(self):
        valor_esperado = "Es un triángulo escaleno."
        valor_actual = evaluar(8, 2, 7)
        self.assertEqual(valor_esperado, valor_actual)
    

if __name__ == '__main__':
    unittest.main()
