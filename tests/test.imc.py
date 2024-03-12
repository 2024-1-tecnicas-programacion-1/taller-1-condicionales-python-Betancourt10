import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.imc import evaluar

class TestIMC(unittest.TestCase):
    def testBajo(self):
        valor_esperado = "Bajo."
        valor_actual = evaluar(50, 1.8,   20)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testMedio(self):
        valor_esperado = "Medio."
        valor_actual = evaluar(76, 1.69,   34)
        self.assertEqual(valor_esperado, valor_actual) 

    def testMedioDos(self):
        valor_esperado = "Medio."
        valor_actual = evaluar(44, 1.7,   52)
        self.assertEqual(valor_esperado, valor_actual) 

    def testAlto(self):
        valor_esperado = "Alto."
        valor_actual = evaluar(70, 1.65,   73)
        self.assertEqual(valor_esperado, valor_actual) 

    def testError(self):
        valor_esperado = "Error."
        valor_actual = evaluar(-2, 1.8,   18)
        self.assertEqual(valor_esperado, valor_actual)
    

if __name__ == '__main__':
    unittest.main()
