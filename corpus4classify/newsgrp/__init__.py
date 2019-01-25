"""
This is the famed 20 Newsgroups dataset. The 'subset' argument can be 'all',
'train', or 'test' as defined by sklearn.
"""
from sklearn.datasets import fetch_20newsgroups

NEWSGROUPS = fetch_20newsgroups(subset='all')


### The API ###
data, target = NEWSGROUPS.data, NEWSGROUPS.target