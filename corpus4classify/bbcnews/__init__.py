"""
Entire model building process:
   1. handle input: read all files into a dict by pointing extract_data to the data location
   2. reshape data: transform dict into 2 lists -- target (type of news) & features (news content)
   3. train model: deep learn on training cases; evaluate OOS prediction accuracy.
   4. return the trained pytorch model object for further analysis.
"""
# from .extract_data import extract_data
# ABS_FILEPATH = Path(__file__).resolve()
# ABS_DIR = ABS_FILEPATH.parents[0]
# ABS_DIR = REL_DIR.resolve()
# import os; os.chdir(str(ABS_DIR))
from .transform_data import reshape
from pathlib import Path

DATA_LOC = Path(__file__).absolute().parent / 'data'
print(DATA_LOC)

def __files2list(files):
   '''Iterates over a files generator. Reads each file as a string. And then append to list.
   '''
   return [file.read_text(errors='ignore') for file in files]

def extract_data():
   '''Go to the dir holding all the data; index the sub-dir names; pack all files in each sub-dir
   into a list. Finally, put the lists in a dict keyed by the sub-dir names.
   '''
   folders = DATA_LOC.iterdir()
   return {folder.stem: __files2list(folder.iterdir()) for folder in folders}

### The API ###
data, target = reshape(extract_data())