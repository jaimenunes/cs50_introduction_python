import os
import sys
import unittest

# Adiciona o diretório pai ao caminho do sistema
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator_two import square

class Test(unittest.TestCase):
    def test_positive(self):
        assert square(3) == 9
        assert square(2) == 4

    def test_negative(self):
        assert square(-2) == 4
        assert square(-3) == 9


    def test_zero(self):
        assert square(0) == 0

    def test_str(self):
        self.assertRaises(TypeError, square, 'cat')
    
if __name__ == "__main__":
    unittest.main()