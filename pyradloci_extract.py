from pathlib import Path
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


inpath='/Users/josec/Desktop/Datasets/skrad/skrad2/ipyrad/skad6_outfiles/skad6.loci'
outpath='/Users/josec/Desktop/Datasets/skrad/skrad2/ipyrad/skad6_outfiles/loci_aln/'
op=Path(outpath)
op.mkdir(exist_ok=True)
instring=Path(inpath).read_text()
lines = instring.split("\n")
recstowrite=[]
for i,line in enumerate(lines):
    if line.startswith('//'):
        phystring='\n'.join(recstowrite)
        #format to fasta
        phystring = phystring.replace('\n','\n>')
        phystring = phystring.replace('     ','\n')
        phystring = '>'+phystring
        phyout=op.joinpath(f'{i}.fasta')
        phyout.write_text(phystring)
        phystring=''
        recstowrite=[]
    else:
        recstowrite.append(line)
