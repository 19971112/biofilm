import sys
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from collections import defaultdict

#argvs = sys.argv
gb_file = sys.argv[1]

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

            # get product
            if 'product' in feature.qualifiers:
                protein = feature.qualifiers['product'][0].replace(' ', '-')
            else:
                protein = 'NA'

            # get organism
            organism = record.annotations['organism']

            # get gene
            gene = feature.qualifiers.get("gene", [""])[0]

            # get locus_tag
            locus = feature.qualifiers['locus_tag'][0]

            #join, chenge list
            classs = record.annotations['taxonomy']
            classs1 = classs[0:3]
            classs2 = '_'.join(classs1)


            #print ('>' + str(i) + '_'+ taxid + '_' + classs2 + '_' + organism + '_' + pseudo)
            #print ('>' + str(i) + '_' + protein + '_' + classs2 + '_' + organism)
            print ('>' + str(i) + '_' + locus + ' ' + protein + '_' + organism)
            print (cds_seq)
            i += 1
