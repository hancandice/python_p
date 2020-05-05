# /Users/candicehan/Documents/doit/sub_dir_search.py

import os
import sys

dir = sys.argv[1]



def sub_dir_search(dir):
    try:
        files = os.listdir(dir)
        for file in files:
            full_filename = os.path.join(dir,file)
            if os.path.isdir(full_filename):
                sub_dir_search(full_filename)
            else:
                extension = os.path.splitext(full_filename)[-1]
                if extension == '.txt':
                    print(full_filename)
 
    except PermissionError:
        pass



    
sub_dir_search(dir)
