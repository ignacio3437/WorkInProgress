#!/usr/bin/python

from pathlib import Path
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
"""
Reads a fasta file and concatenates sequences with
the same name in the order they appear in the infile.
Also writes a fasta file named dedupe_infile that has
all of the repeated fasta headers with suffixes.
"""


def dedupe_and_read_fasta(infile):
    text = str(infile.read_text())
    headers = []
    for line in text.split('\n'):
        if line.startswith('>'):
            suffix = 0
            new_line = f'{line}_{suffix}'
            if new_line in headers:
                while new_line in headers:
                    suffix +=1
                    new_line = f'{line}_{suffix}'
                headers.append(new_line)

            else:
                headers.append(new_line)
            text = text.replace(f'{line}\n',f'{new_line}\n',1)
    dedupe_path = Path(infile.parent/f'dedupe_{infile.name}')
    dedupe_path.write_text(text)
    records = list(SeqIO.parse(str(dedupe_path), "fasta"))

    return records


def concater(records,infile):
    concat_records = []
    genelist=set([record.name.split('_')[0] for record in records])
    gene_dict={}
    for record in records:
        gene_name,dud,exon=record.name.split('_')
        if gene_name in gene_dict:
            gene_dict[gene_name].append(record.seq)
        else:
            gene_dict[gene_name]=[record.seq]
    for gene,seqs in gene_dict.items():
        concatenated = Seq("", generic_dna)
        for s in seqs:
            concatenated += s
        to_add = SeqRecord(concatenated,id=gene,name=gene,description="")
        concat_records.append(to_add)
        # print(concatenated)
    concat_path = Path(infile.parent/f'concat_{infile.name}')
    SeqIO.write(concat_records,str(concat_path),'fasta')
    # concat_path.write_text(concat_records)


    return

def main():
    infile=Path("/Users/josec/Desktop/BaitV2Assembly.fasta")
    records=dedupe_and_read_fasta(infile)
    concater(records,infile)
    # metadict,genelist=metadicter(fastdict)
    # metparse(metadict,genelist)



if __name__ == '__main__':
    main()
