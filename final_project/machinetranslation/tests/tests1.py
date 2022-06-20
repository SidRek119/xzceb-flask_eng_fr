import unittest
from translator import english_to_french, french_to_english

class Test_English_To_French(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french("Dog"),"Bonjour") # test when no input
        self.assertEqual(english_to_french("Hello"),"Bonjour")  # test when  "Hello" is given as input

class Test_french_To_English(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english("Merci"),"Goodbye") # test when no input
        self.assertEqual(french_to_english("Bonjour"),"Hello") # test when  "Bonjour" is given as input
unittest.main()
