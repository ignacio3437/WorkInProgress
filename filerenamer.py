import os
import shutil
old_list=[]
new_list=[]
wd="/Users/josec/Desktop/renaming/PilbaraNCB240C_F"
codex_file="/Users/josec/Desktop/renaming/CF.txt"
newd="/Users/josec/Desktop/renaming/PilbaraNCB240C_F_renamed"

codex_dictionary={}
with open(codex_file, "Ur") as codex:
    for line in codex:
        linelist=line.split(",")
        codex_dictionary[linelist[0]]=linelist[1].strip("\n")

try:
    os.mkdir(newd)
except:
    pass
for f in os.listdir(wd):
    ofilename= f.split(".")[0]
    ofilepath= os.path.join(wd,f)
    if ofilename in codex_dictionary:
        nfilename= codex_dictionary[ofilename]
        handlepath=ofilepath.replace(ofilename,nfilename)
        nfilepath=os.path.join(newd,os.path.basename(handlepath))
        if handlepath.endswith("fa") or handlepath.endswith("seq"):
            rename_content=True
        else:
            rename_content=False
        if rename_content:
            with open(ofilepath,"Ur") as efile:
                old_file_string=efile.read()
                new_file_string=old_file_string.replace(ofilename,nfilename)
            with open(nfilepath,"w") as fileout:
                fileout.write(new_file_string)
        else:
            shutil.copy(ofilepath,nfilepath)
