import os
import shutil
wd="/Users/josec/Desktop/ChromEx/ChromEx3/ChromEx3_Trim_aln"
pull_file="/Users/josec/Desktop/ChromEx/ChromEx3/Teas_Chromex3.txt"
newd="/Users/josec/Desktop/ChromEx/ChromEx3/Teasdale_ChromEx3"

pull_list=[]
with open(pull_file, "Ur") as pull_handle:
    for line in pull_handle:
        pull_list.append(line.rstrip('\n'))
# print pull_list

try:
    os.mkdir(newd)
except:
    pass
for f in os.listdir(wd):
    ofilename= f.split(".")[0].lstrip('TRIM_')
	#ofilename= f.split(".")[0]
    if ofilename in pull_list:
        shutil.copy("%s/%s"%(wd,f),"%s/%s"%(newd,f))