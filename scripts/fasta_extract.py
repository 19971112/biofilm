import sys
from Bio import SeqIO

args = sys.argv

fasta_in = args[1]
query = args[2]

for record in SeqIO.parse(fasta_in, 'fasta'):
   if record.id == query:
      print(">",record.description)
      print(record.seq)
      break
