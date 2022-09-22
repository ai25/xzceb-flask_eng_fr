from translator import english_to_french, french_to_english
import unittest

class Test(unittest.TestCase):
    def test_not_null_e2f(self):
        self.assertNotEqual(english_to_french('Hello'), None)
    def test_translate_e2f(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    
class Test2(unittest.TestCase):
    def test_not_null_f2e(self):
        self.assertNotEqual(french_to_english('Bonjour'), None)
    def test_translate_f2e(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')

if __name__ == "__main__":
    unittest.main()
