import pandas as pd
import glob, os

cutoff = 10**20

df = pd.read_csv("parsed/PMID_pubYear.csv", nrows=cutoff)

df['has_ack'] = False
known_PMC = set(df.PMCID.values)
df = df.set_index("PMCID")


f = 'results/PMC_ack_stats.csv'    
info = pd.read_csv(f,usecols=['filename'], nrows=cutoff).filename
info = info.apply(os.path.basename).str.split('.').str[0]


has_PMC = info.str[:3] == "PMC"
info = info[has_PMC]
    
idx = info.isin(known_PMC).values
info = info[idx]
    
df.loc[info.values, 'has_ack'] = True
print(f, idx.mean(), df.has_ack.mean(), df.has_ack.sum())

df.to_csv("parsed/PMID_PMCID_pubYear.csv")


##############################################################
exit()

for f in glob.glob("extracted/articles.*"):
    info = pd.read_csv(f,usecols=['filename'], nrows=cutoff).filename
    info = info.apply(os.path.basename).str.split('.').str[0]

    has_PMC = info.str[:3] == "PMC"
    info = info[has_PMC]
    #info = info.str[3:].values

    idx = info.isin(known_PMC).values
    info = info[idx]
    
    df.loc[info.values, 'has_ack'] = True
    print(f, idx.mean(), df.has_ack.mean())

df.to_csv("parsed/PMID_PMCID_pubYear.csv")
