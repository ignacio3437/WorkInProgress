#!/usr/bin/python3
import os
import sys
# import re
# import shutil

# from pathlib import Path



'''

'''

usage = """python filerenamer.py --dir directory_with_files_to_rename --codex csv_of_how_to_rename.txt


Renames every file specified in --dir that contains the key specified in --codex. 

Example of Codex file:
old,new

Would change Picture_of_old_house.jpg to Picture_of_new_house.jpg 
"""


def codexdicter(codex_file):
    with open(codex_file,'r') as codex_handle:
        codex=codex_handle.read()
    clist=codex.split('\n')
    codexdict={}
    for c in clist:
        pair=c.split(',')
        codexdict[pair[0]]=pair[1]
    return codexdict

def driver(indir,codex_file):
    pwd=indir+"/"
    codexdict = codexdicter(codex_file)
    #outdir = indir+"_renamed"
    for k in codexdict.keys():
        for filename in os.listdir(indir): 
            if k in filename:
                new_filename = filename.replace(k,codexdict[k])
                os.rename(pwd+filename, pwd+new_filename)
    print("done")
    return 

def main():
    args = sys.argv[1:]
    # args = ["--dir", "/home/iggy/BioinformatIg/Coral/Trimmed", "--codex", "/home/iggy/BioinformatIg/Coral/Sample_Codex.txt" ] # For Testing
    if not args:
            print(usage)
            sys.exit(1)
    if args[0] == '--dir' and args[2] == '--codex':
        driver(indir=args[1],codex_file=args[3])
    else:
        print(usage)    
        sys.exit(1)
    return

if __name__ == "__main__":
    main()