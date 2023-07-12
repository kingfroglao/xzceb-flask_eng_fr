import unittest

from translator import french_to_english
from translator import english_to_french


class TestE2F(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Bye'), 'Au revoir')
        
    
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Bye')

unittest.main()
