import pandas as pd

df = pd.read_csv('/Users/jonesgd/projects/hackathon/data/articles.A-B.xml.tar.gz_reduced.csv', index_col=0)
df2 = pd.read_csv('/Users/jonesgd/projects/hackathon/data/articles.C-H.xml.tar.gz_reduced.csv', index_col=0)
df3 = pd.read_csv('/Users/jonesgd/projects/hackathon/data/articles.I-N.xml.tar.gz_reduced.csv', index_col=0)
df4 = pd.read_csv('/Users/jonesgd/projects/hackathon/data/articles.O-Z.xml.tar.gz_reduced.csv', index_col=0)

lst = [
    [df,'articles.A-B.xml.tar.gz_cleaned.csv'],
    [df2,'articles.C-H.xml.tar.gz_cleaned.csv'],
    [df3,'articles.I-N.xml.tar.gz_cleaned.csv'],
    [df4,'articles.O-Z.xml.tar.gz_cleaned.csv']
]

journal = pd.DataFrame()

for x,y in lst:
    print(x)
    journal = x['filename'].str.split(pat='/', expand=True)
    journal = journal.rename({0:'journal', 1:'PMCID'}, axis=1)
    pmcid = journal['PMCID'].str.split(pat='.', expand=True)
    pmcid = pmcid.drop(labels={1}, axis=1)
    df5 = pmcid[0].str.split(pat='PMC', expand=True)
    journal['PMCID'] = df5[1]
    journal['ack_present'] = x['ack_present']
    print(journal)
    journal.to_csv(y, index=False)


exit()
