import sys
import glob
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from collections import defaultdict

gb_file = glob.glob('*.gbff')

print("FileName", "#ofCDSs","Taxid", "Taxnomy", "OrganismName",sep="\t")

for file in gb_file:
    i = 0
    for record in SeqIO.parse(file, 'genbank'):
        for feature in record.features:
            ### GET TAXID
            if feature.type == 'source':
                for xref in feature.qualifiers['db_xref']:
                    if xref[0:6] == 'taxon:':
                        taxid = xref[6:]
            ### get annotation
            classs = record.annotations['taxonomy']
            classs1 = classs[0:6]
            annotation = '_'.join(classs1)
            ### get organism name
            organism = record.annotations['organism']
            ### CDS count
            if feature.type == 'CDS':
                i += 1
    print(file, i,taxid, annotation, organism,sep="\t")
