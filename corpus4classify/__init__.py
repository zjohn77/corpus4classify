def getdata(corpus):
   '''Pick the corpus to load by supplying the "corpus" argument.
   '''
   if corpus == 'bbcnews':
      from .bbcnews import data, target
   elif corpus == 'newsgrp':
      from .newsgrp import data, target
   else:
      raise Exception("Corpus not found.")

   return data, target