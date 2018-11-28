#!/usr/bin/python
import os,sys,re

# filein=os.path.abspath('/Users/josec/Desktop/ChromEx3_Astral/quartet_support_Chromex3_astral.tre')

args = sys.argv[1:]
filein = sys.argv[1]
usage = "usage: python3 /Path/2/renamer_nudi.py file2rename"





filename=os.path.basename(filein)
pwd=os.path.dirname(filein)
rfilename="r_"+filename

codex="""CASIZ192287,CASIZ192287_aff_aspersa
CASIZ192279,CASIZ192279_aff_aspersa
CASIZ176754,CASIZ176754_aff_elisa_A
UF305137,UF305137_aff_elisa_B
CASIZ121007,CASIZ121007_aff_elisa_B
CASIZ181260,CASIZ181260_aff_manda
WAMS96283,WAMS96283_aff_stria_WA_A
WAMS99380,WAMS99380_aff_stria_WA_B
WAMS35107,WAMS35107_aff_stria_WA_B
WAMS56055,WAMS56055_aff_willani
CASIZ177260,CASIZ177260_aff_willani
CASIZ194439,CASIZ194439_africana
CASIZ194460,CASIZ194460_africana
CASIZ204143,CASIZ204143_annae
WAMS67522,WAMS67522_annae
CASIZ191422,CASIZ191422_aspersa
WAMS67676,WAMS67676_aspersa
WAMS103006,WAMS103006_burni
WAMS103007,WAMS103007_burni
WAMS70791,WAMS70791_cf_africana
CASIZ177426,CASIZ177426_cf_burni
CASIZ177428,CASIZ177428_cf_burni
WAMS67532,WAMS67532_cf_dianae
WAMS67536,WAMS67536_cf_dianae
SBMNH89038,SBMNH89038_cf_lochi_FP
UF400236,UF400236_cf_lochi_FP
WAMS67573,WAMS67573_cf_lochi_FPV
UF368685,UF368685_cf_lochi_FPV
WAMS103008,WAMS103008_cf_stria_QLD
CASIZ177676,CASIZ177676_cf_stria_spot
WAMS35075,WAMS35075_colemani
CASIZ177266,CASIZ177266_colemani
WAMS67533,WAMS67533_dianae
CASIZ177242,CASIZ177242_dianae
WAMS67521,WAMS67521_elisabethina
WAMS67542,WAMS67542_elisabethina
CASIZ194415,CASIZ194415_hamiltoni
CASIZ194587,CASIZ194587_hamiltoni
WAMS67657,WAMS67657_joshi
CASIZ217220,CASIZ217220_joshi
WAMS103139,WAMS103139_kuiteri
WAMS67546,WAMS67546_kuiteri
UF310537,UF310537_lineolata
WAMS67527,WAMS67527_lineolata
WAMS67566,WAMS67566_lochi
CASIZ182290,CASIZ182290_lochi
WAMS92170,WAMS92170_magnifica
CASIZ204796,CASIZ204796_magnifica
CASIZ194453,CASIZ194453_mandapamensis
CASIZ182807,CASIZ182807_michaeli
MMRBK457,MMRBK457_orientalis
CASIZ192286,CASIZ192286_quadricolor
WAMS67596,WAMS67596_sp_IP
CASIZ204798,CASIZ204798_sp_meso
CASIZ204797,CASIZ204797_sp_meso
CASIZ192505,CASIZ192505_sp_SA
WAMS99382,WAMS99382_striatella
AMC415149C,AMC415149C_striatella
WAMS103147,WAMS103147_strigata
CASIZ199453,CASIZ199453_strigata
WAMS56037,WAMS56037_westraliensis
WAMS92252,WAMS92252_westraliensis
CASIZ202316,CASIZ202316_willani
WAMS67603,WAMS67603_willani
WAMS92135,WAMS92135_G_fidelis
WAMS92136,WAMS92136_G_coi
WAMS92138,WAMS92138_D_atromarginata
WAMS103020,WAMS103020_A_egretta
WAMS103005,WAMS103005_C_colemani"""
clist=codex.split('\n')
codexdict={}
for c in clist:
    pair=c.split(',')
    codexdict[pair[0]]=pair[1]

with open(filein,'r') as filein:
    with open(os.path.join(pwd,rfilename),'w') as fileout:
        instring=filein.read()
        # fileout.write(instring)
        for key in codexdict:
            instring=instring.replace(key,codexdict[key])
        # fileout.write("\n\n\n")
        instring=instring.replace("CHANGE","")
        fileout.write(instring)
print("done")
