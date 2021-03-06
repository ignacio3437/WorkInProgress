#!/usr/bin/python

"""
For single use.Reads a fasta file
concats exons together but seperates by gene and organism.
Input:
>gene-exon-org
ACTGSEQ

Output:
>org_gene
ACTGSEQ (concatenated in correct exon order)
"""

def fastadicter(input):
	inputf= open(input, 'Ur')
	fastdict={}
	faslines = inputf.readlines()
	for i,line in enumerate(faslines):
		if i ==0:
			nel=0
		if '>' in line:
			if nel:
				fastdict[fasname]=nel
			fasname = line.strip('>').rstrip('\n')
			nel=0
		else:
			nel=line
		if i ==len(faslines)-1:
			fastdict[fasname]=nel
		fastdict[fasname]=nel
	inputf.close()
	return fastdict

def metadicter(fastdict):
	metadict={}
	genelist=[]
	for key in fastdict.keys():
		ks=key.split("-")
		gene=ks[0]
		rdkeys=['seq','exon','org','gene']
		print gene
		rdvals=[fastdict[key].strip('\n'),float(ks[1]),ks[2],gene]
		if gene not in genelist:
			genelist.append(gene)
			metadict[gene]=[dict(zip(rdkeys,rdvals))]
		else:
			metadict[gene].append(dict(zip(rdkeys,rdvals)))
	return metadict,genelist


def metparse(metadict,orgs,genelist):
	outhandle=open('/Users/josec/Desktop/New_Ref_gen/SpurCDS_Trim2Targets_concat.fa','w')
	for gene in genelist:
		for org in orgs:
			exon_list=[]
			hit_list=[]
			for hit in metadict[gene]:
				if hit['org']==org:
					exon_list.append(hit['exon'])
					hit_list.append(hit)
			exon_list.sort()
			if len(exon_list)>0:
				to_write=[">%s-%s\n"%(org,hit['gene'])]
				for exon in exon_list:
					for hit in hit_list:
						if hit['exon']==exon:
							to_write.append(hit['seq'])
			outhandle.write(''.join(to_write))
			outhandle.write('\n')
	outhandle.close()
	#comment out the rest if you dont want a seqlength count
	# outhandle=open('/Users/josec/Desktop/cons_ordered.fasta','rU')
	# outlines=[x.strip('\n') for x in outhandle.readlines()]
	# name=''
	# seq_length=''
	# for out in outlines:
	# 	if '>' in out:
	# 		name=out
	# 	else:
	# 		seq_length=len(out)
	# 		print name+'\t'+str(seq_length)
	return



def main():
	#orgs=['Met','Crino','Cya','Oligo']
	orgs=['Spur']
	input="/Users/josec/Desktop/New_Ref_gen/NewRef1.fasta"
	fastdict=fastadicter(input)
	metadict,genelist=metadicter(fastdict)
	metparse(metadict,orgs,genelist)



if __name__ == '__main__':
	main()
