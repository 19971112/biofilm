import pandas as pd

File1 = "cds-count.txt"
Level = 2

df = pd.read_table(File1, header=0)
df["Class"] = df['Taxnomy'].str.split(pat='_', expand=True)[Level]

df2 = df.loc[:,["#ofCDSs","Class"]]
df2.set_index('Class', inplace = True)
df3 = df2.groupby(level=0).sum()

df3.to_csv('cds-count-sort.txt', header=True, index=False, sep='\t')
