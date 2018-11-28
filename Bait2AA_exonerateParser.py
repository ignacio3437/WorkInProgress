#!/usr/bin/python

import os
import re

"""
Parses an exonerate run where the:
Query: S pur. AA gene targets
Target: Concatenated Crinoid Bait DNA sequences
Model: Protein2DNA
ryo format name: 'QueryID:TargetID:Hit_start:Percent_ID:seq'
ryo format seq: Parts of query that match the target. (ie the parts of the S pur. AA gene that were targeted)

Command
exonerate --model protein2genome -q Nov_SpurGenes_aa.fasta -t concat_Bait.fasta -Q AA -T DNA --showvulgar F --showalignment F --verbose 0 --ryo '>%qi:%ti:%qab:%ps:%qas\n' > SpurAACriDNA_exonerate_p2g.txt

The output is the ryo format seq concatenated by exon order.
"""

input_path=os.path.abspath("/Users/josec/Desktop/Crinoid_capture/Dec_HybTxCrinoid/SpurAACriDNA_exonerate_p2g.txt")
concat_output_path=os.path.abspath("/Users/josec/Desktop/Crinoid_capture/Dec_HybTxCrinoid/SpurAACriDNA_targets.fa")
manually_curate_path=os.path.abspath("/Users/josec/Desktop/Crinoid_capture/Dec_HybTxCrinoid/To_curate.fa")
out_handle=open(concat_output_path,'w')
manout_handle=open(manually_curate_path,'w')

filtered_hits=[]
gene_list=[]
manually_curate_list=[]


with open(input_path,'ru') as in_handle:
    in_string=in_handle.read()

exonerate_hits=[hit.rstrip('\n') for hit in in_string.split('>')]

for hit in exonerate_hits:
    #Check if blank hit
    if len(hit)>10:
        qid,tid,start,pid,seq=hit.split(':')
    else:
        continue

    #filter parameters
    if qid==tid and float(pid)>75:
        #remove new lines inside of the sequence and add to filtered_hits list
        filtered_hits.append("%s:%s:%s"%(qid,start,re.sub('\n','',seq)))
        #making a list of genes for later
        if qid not in gene_list:
            gene_list.append(qid)

for gene in gene_list:
    breaker=True
    gene_hits=[]
    for hit in filtered_hits:
        if gene in hit:
            gene_hits.append(hit)
#Sort the hits by the start position(ie transcription order)
    sorted_gene_hits=sorted(gene_hits, key=lambda hit: int(hit.split(':')[1]))


#Check if there is overlap between the hits. If so add to file to manually curate later
#If there is an overlap problem it will trip the breaker and skip this gene in the output
    starts=[int(hit.split(':')[1]) for hit in sorted_gene_hits]
    lengths=[len(hit.split(':')[2]) for hit in sorted_gene_hits]
    for x in range(len(sorted_gene_hits)):
        try:
            if starts[x]+lengths[x]>starts[x+1]:
                breaker=False
                manually_curate_list.append(sorted_gene_hits)
        except:
            pass
    if breaker:
        if len(sorted_gene_hits)>1:
            seq_to_print=[hit.split(':')[2] for hit in sorted_gene_hits]
            out_handle.write(">%s\n%s\n"%(sorted_gene_hits[0].split(':')[0],''.join(seq_to_print)))
        else:
            singleton=sorted_gene_hits[0]
            out_handle.write(">%s\n%s\n"%(singleton.split(':')[0],singleton.split(':')[2]))
for gene in manually_curate_list:
    for frag in gene:
        qid,start,seq=frag.split(":")
        manout_handle.write(">%s_%s\n%s\n"%(qid,start,seq))
    manout_handle.write("\n\n\n\n")


out_handle.close()
manout_handle.close()
