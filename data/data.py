"""data.py

Simple script to validate the downloaded data:
 - ds005
 - ds005_filtered
 - ds114
"""

import pdb
import json

from data_hashes import check_hashes 

if __name__ == "__main__":
#TODO: add the folder ds005 here
    file_ls = ['ds005_filtered_hashes.json',\
              # 'ds005_hashes.json',\
               'ds114_hashes.json']
    for f in file_ls:
        with open(f) as infile:
            f_dict = json.load(infile)
            check_hashes(f_dict)
