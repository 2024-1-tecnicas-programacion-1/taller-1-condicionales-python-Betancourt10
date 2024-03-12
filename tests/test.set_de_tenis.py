import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.set_de_tenis import evaluar

class TestSetDeTenis(unittest.TestCase):
    def test_aun_no_termina(self):
        valor_esperado = "Aún no termina."
        valor_actual = evaluar(4, 5)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_gano_a(self):
        valor_esperado = "Ganó A."
        valor_actual = evaluar(7, 5)
        self.assertEqual(valor_esperado, valor_actual) 

    def test_gano_b(self):
        valor_esperado = "Ganó B."
        valor_actual = evaluar(3, 6)
        self.assertEqual(valor_esperado, valor_actual) 

    def test_error(self):
        valor_esperado = "Error."
        valor_actual = evaluar(-3, 5)
        self.assertEqual(valor_esperado, valor_actual) 

    def test_invalido(self):
        valor_esperado = "Inválido."
        valor_actual = evaluar(8, 6)
        self.assertEqual(valor_esperado, valor_actual) 

    def test_gano_a_dos(self):
        valor_esperado = "Ganó A."
        valor_actual = evaluar(7, 6)
        self.assertEqual(valor_esperado, valor_actual) 

    def test_gano_b_dos(self):
        valor_esperado = "Ganó B."
        valor_actual = evaluar(6, 7)
        self.assertEqual(valor_esperado, valor_actual)
    

if __name__ == '__main__':
    unittest.main()
