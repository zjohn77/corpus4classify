def controller(corpus):
   if corpus == 'bbcnews':
      from .bbcnews import data, target
   elif corpus == 'newsgrp':
      from .newsgrp import data, target
   else:
      raise Exception("Example not found.")

   return data, target