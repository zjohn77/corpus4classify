"""
Test the bbcnews module's functions: extract_data, reshape. 
"""
from unittest import TestCase
from pathlib import Path
import sys; sys.path.insert(0, 
                            Path(__file__).parents[1]
                           )
from corpus4classify.bbcnews import extract_data, reshape

class Usage(TestCase):
   @classmethod
   def setUpClass(cls):
      cls.EXTRACT = extract_data()
   
   def test_extract_data(self):
      '''Should traverse the directory; load all files into a dict 
      with 5 keys corresponding to the 5 folders under "data/".
      '''
      self.assertEqual(set(Usage.EXTRACT.keys()),
                       {'tech', 'sports', 'politics', 'business', 'entertainment'}
                      )

   def test_reshape(self):
      '''Should convert a wide dataframe to a narrow dataframe through the use of an
      indicator column (the 2nd column here).
      '''
      DATA = {'arts': [4],
              'tech': [6, 9]
             }
      self.assertTrue(reshape(DATA) == ([4, 6, 9], 
                                        [0, 1, 1]
                                       )
                     )