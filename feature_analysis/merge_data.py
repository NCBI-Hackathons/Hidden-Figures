import pandas as pd
from tqdm import tqdm


df = pd.read_csv('articles.A-B.xml.tar.gz_cleaned.csv', usecols={'journal','PMCID','ack_present'})
df2 = pd.read_csv('articles.C-H.xml.tar.gz_cleaned.csv', usecols={'journal','PMCID','ack_present'})
df3 = pd.read_csv('articles.I-N.xml.tar.gz_cleaned.csv', usecols={'journal','PMCID','ack_present'})
df4 = pd.read_csv('articles.O-Z.xml.tar.gz_cleaned.csv', usecols={'journal','PMCID','ack_present'})


merged = pd.concat([df, df2,df3,df4], ignore_index=True).dropna(subset=['PMCID'])#.set_index('PMCID')

print(merged['PMCID'].isna().sum())

merged['PMCID'] = merged['PMCID'].astype(int)
print(merged)

merged = merged.drop_duplicates(subset=["PMCID"]).set_index('PMCID')

print(merged)


merge_cols = ['Pub Year', 'MeSH Keywords', 'MeSH Extracted','RCR','Journal Name']

for col in merge_cols:
    merged[col] = None

pub_data = pd.read_csv('PMC_info-iSearch_-_Publications-export_2018-09-04-20-53-47.csv',
    chunksize=5000)

for x in tqdm(pub_data, total=2000000//5000):
    x['PMCID'] = x['PMCID'].str[3:]
    x['PMCID'] = x['PMCID'].str.split(pat=".", expand=True)[0]
    x = x[x['PMCID'].str.isnumeric() == True]
    x['PMCID'] = x['PMCID'].astype(int)
    #print(x['PMCID'])
    x = x.drop_duplicates(subset=["PMCID"]).set_index("PMCID")

    idx = x.index.isin(merged.index)
    x = x[idx]

    #print(len(x))
    #continue

    assert(x.index.isna().sum() == 0)
    for col in merge_cols:
        merged.loc[x.index, col] = x.ix[x.index, col].values
        #print(merged[merged['Pub Year'].isna() == False])
    #print(merged)
    print(merged['Pub Year'].isna().mean())


merged.to_csv("articles.merged_with_data.csv")


exit()






'''
['Cross Ref ID', 'DOI', 'NLM Unique Id', 'PMCID', 'PMID', 'Pub Date', 'Pub Types', 'Pub Year',
'Title', 'MeSH Keywords', 'MeSH Extracted', 'Substances', 'Condition', 'Chemicals & Drugs', 'Devices',
'Target', 'Authors', 'Author First Name', 'Author Last Name', 'Authors Initials', 'Full Author Affiliation',
'Author Affiliation', 'Author Location', 'First Author', 'Last Author', 'iCite Article Type',
'iTrans Cited By', 'iTrans Clinical', 'Animal', 'APT Score', 'Article Citation Rate',
'Expected Citation Rate', 'Field Citation Rate', 'Human', 'Journal Citation Rate',
'Mol/Cell', 'RCR', 'Total Citations', 'Total References', 'Grant Number', 'Activity Code',
'PCC', 'RFA/PA Number', 'RFA/PA Title', 'Admin IC', 'Appl ID', 'Fiscal Year', 'Funding Agency',
'Patent ID', 'Clinical Trial', 'ISSN', 'Journal Country', 'Journal Issue', 'Journal Name',
'Journal Name ISO', 'Journal Pages', 'Journal Volume', 'Journal Id', 'System ID']
'''
