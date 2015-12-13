"""get_ds005_hashes_from_txt.py
Creates a .json file with hashes for our ds005 data from text file
containing file names and corresponding hashes.

Run wuth:
    python get_ds005_hashes_from_txt.py
"""
from __future__ import print_function
from data_hashes import create_dict 
import json
import pdb

def create_dict(filename):
    """Return a dictionary of hashes from a .txt file

       Parameters
       ----------
       filename: .txt file containing the each file hash in the
           first column and the file location in the data in the
            second column.
       Returns
       ---------
       newDict: a dictionary of hashes
    """
    newDict={}
    f=open(filename)
    num_lines = sum(1 for line in open(filename))
    for line,i in zip(f,range(0,num_lines)):
        info = line.split()
        newDict[info[1]]=info[0]
    f.close()
    return newDict

#For our data ds005
newDict = create_dict('ds005_raw_checksums.txt')
with open('ds005_hashes_checksums.json', 'w') as file_out:
    json.dump(newDict, file_out)
#    print(check_hashes(newDict))
