"""
Create a new file called tests.py in the machinetranslation directory.
Write at least 2 tests in tests.py for each method
Test for null input for frenchtoenglish
Test fot full input for englishToFrench.
Test for the translation of the word ‘Hello’ and ‘Bonjour’.
Test for the translation of the word ‘Bonjour’ and ‘Hello’.
Take a screenshot of your unit tests and save it 
as a .jpg or .png with the filename translation_unittests.
"""

import unittest

from translator import frenchtoenglish, englishtofrench


class EnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')
        self.assertIsNotNone(englishtofrench('I'))


class FrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')
        self.assertIsNotNone(frenchtoenglish('Je'))


unittest.main()
