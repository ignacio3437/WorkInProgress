#!/usr/local/bin/python3

from pathlib import Path
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
"""


"""

##SET VARIABLES
RefSeq_CDS_pstring='/Users/jose.carvajal/Desktop/exoncap/Mygal/PseudoRefGen/6_refseqcds_loci.fas'
ExonsTargeted_pstring='/Users/jose.carvajal/Desktop/exoncap/Mygal/PseudoRefGen/BaitNames_nostop.txt'
Exon_folder_pstring='/Users/jose.carvajal/Desktop/exoncap/Mygal/PseudoRefGen/9_cds_exon_folder'
outfile='/Users/jose.carvajal/Desktop/exoncap/Mygal/PseudoRefGen/PseudoRef.fas'


def exon_dict_generator(ExonsTargeted_pstring):
    # constructs exon_dict so that
    # exon_dict[targeted_gene]=list of exon numbers targeted
    exonstargeted_string = Path(ExonsTargeted_pstring).read_text()
    exon_lines = exonstargeted_string.split("\n")
    exon_dict = {}
    for line in exon_lines:
        XPcode, exon_num = line.split('_')[1:3]
        if XPcode in exon_dict:
            exon_dict[XPcode].append(exon_num)
        else:
            exon_dict[XPcode] = [exon_num]
    return exon_dict

def seq_dict_generator(Exon_folder_pstring):
    # constructs seq_dict so that
    # seq_dict[targeted_gene]= SeqIOdict
    # SeqIOdict[gene_exonnumber]= exonseq
    path = Path(Exon_folder_pstring)
    seq_dict = {}
    for p in path.rglob("*.fas"):
        genename = p.name.replace(".fas","").replace(".2","").replace(".1","")
        seq_dict[genename] = SeqIO.to_dict(SeqIO.parse(p, "fasta"))
    return seq_dict





#TESTING
seq_dict = seq_dict_generator(Exon_folder_pstring)
exon_dict = exon_dict_generator(ExonsTargeted_pstring)
# print(seq_dict['XP_021004583.1']['XP_021004583_1'].name)


outfasta_string=""
for tar_gene in exon_dict.keys():
    seq_string = ""
    gene_name=f"XP_{tar_gene}"
    num_exons = len(seq_dict[gene_name])
    for i in range(num_exons):
        ex_seq = seq_dict[gene_name][f"{gene_name}_{i}"].seq
        if str(i) in exon_dict[tar_gene]:
            seq_string += ex_seq
        else:
            N2add = len(ex_seq)%3
            seq_string += "N"*N2add
    outfasta_string += f">{gene_name}\n{seq_string}\n"
p = Path(outfile)
p.write_text(outfasta_string)




