import unittest
from translator import english_to_french,french_to_english

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('NULL'),'NULL') #test to check null input sould give null output
        self.assertEqual(english_to_french('Hello'),'Bonjour') # test to check proper output
        self.assertNotEqual(english_to_french('Hello'),'Hello')

class TestengfrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('NULL'),'NULL') #test to check null input sould give null output
        self.assertEqual(french_to_english('Bonjour'),'Hello') # test to check proper output
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')      
unittest.main()
