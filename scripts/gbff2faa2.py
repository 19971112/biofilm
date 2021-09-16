import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from collections import defaultdict

argvs = sys.argv
gb_file = argvs[1]

i = 1
for record in SeqIO.parse(gb_file, 'genbank'):

    for feature in record.features:
        pseudo = '0'

        ### GET TAXID
        if feature.type == 'source':
            for xref in feature.qualifiers['db_xref']:
                if xref[0:6] == 'taxon:':
                    taxid = xref[6:]

        ### PSEUDO CHECK
        if feature.type == 'CDS':
            if 'pseudo' in feature.qualifiers:
                pseudo = '1'
                continue

            ## FOR NUC
            #parental_seq = record.seq
            #geneseq = str(feature.location.extract(parental_seq))

            if 'translation' in feature.qualifiers:
                cds_seq = (feature.qualifiers['translation'][0])

            #if 'product' in feature.qualifiers:
            #    protein = (feature.qualifiers['product'][0])


            if 'product' in feature.qualifiers:
                protein = feature.qualifiers['product'][0]
            else:
                protein = 'NA'

            #for xref in feature.qualifiers['db_xref']:
                #if xref[0:6] == 'GeneID:':
                    #geneid = xref[6:]

            #join, chenge list
            classs = record.annotations['taxonomy']
            classs1 = classs[0:5]
            classs2 = '_'.join(classs1)
            locus = feature.qualifiers['locus_tag'][0]

            organism = record.annotations['organism']

            #print ('>' + str(i) + '_'+ taxid + '_' + classs2 + '_' + organism + '_' + pseudo)
            print ('>' + str(i) + '-'+ locus + '-' + taxid + '-' + classs2 + '_' + organism + '_' + protein)
            #print ('>' + str(i) + '_' + protein + '_' + classs2 + '_' + organism)
            print (cds_seq)
            i += 1
