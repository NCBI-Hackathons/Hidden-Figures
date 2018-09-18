import pandas as pd
from unidecode import unidecode
from tqdm import tqdm

cutoff = 10**20
f_save = "parsed/single_named_sentences.csv"

gender = pd.read_csv(
    "../source_data/genderizer_collected.csv",
).dropna()
gender["name"] = gender.name.apply(unidecode).str.lower()
gender = gender.drop_duplicates(subset=["name"])
gender["score"] = None

# Assign a single "score" 1.0 for 100% female, 0.0 for 100% male
idx = gender.gender=="female"
gender.loc[idx, "score"] = gender.loc[idx, "probability"]
gender.loc[~idx, "score"] = 1 - gender.loc[~idx, "probability"]
known_names = set(gender.name.values)
gender = gender.set_index("name")

cols = ["PMCID", "Author Last Name"]

PMC = pd.read_csv(
    "../source_data/PMC_info-iSearch_-_Publications-export_2018-09-04-20-53-47.csv",
    nrows=cutoff,
    usecols=cols
)

df = pd.read_csv(
    "parsed/sentences_with_at_least_one_name.csv",
    nrows=cutoff,
)

# Clean the PMCID field in df to just the numeric part and set the index
df["PMCID"] = df.filename.str.split('/').apply(lambda x:x[-1])
df["PMCID"] = df.PMCID.str.split('.').apply(lambda x:x[0])
df["PMCID"] = df.PMCID.str[3:].astype(int)
#df = df.set_index("PMCID", drop=False)

# Clean the PMCID field in PMC to just the numeric part and set the index
PMC["PMCID"] = PMC["PMCID"].str[3:]

# Find those IDs that are not fully numeric
idx0 = PMC.PMCID.str.find('.') == -1
idx1 = PMC.PMCID.str.find('_') == -1
PMC = PMC[idx0 & idx1]

PMC.PMCID = PMC.PMCID.astype(int)
PMC = PMC.set_index("PMCID")


# Just take the overlap of the dataframes
idx = PMC.index.isin(df.PMCID)
PMC = PMC[idx]
print(f"Rows in PMC dataframe {len(PMC)}")

idx = df.PMCID.isin(PMC.index)
df = df[idx]
print(f"Rows in ACK dataframe {len(df)}")


def parse_name_list(names):
    # Build a list of the names from ; separated list
    # unidecode, lower-cased, and only the last token
    
    names = [x.split()[-1] for x in names.split(';') if x]
    names = map(str.lower, map(unidecode, names))
    return list(names)

data = []
for k, row in tqdm(df.iterrows(), total=len(df)):

    # Simple filter to remove more support sentences
    if "was supported by" in row.sentence.lower():
        continue
    
    pmcid = row.PMCID
    key = 'Author Last Name'
    
    author_last_names = set(parse_name_list(PMC.loc[pmcid,key]))
    ack_last_names = parse_name_list(row.names)

    # Find out which last names are in both the ack and author list
    overlap_index = [
        ack_last_names.index(name) for name in
        author_last_names.intersection(ack_last_names)
    ]

    # Remove those names
    filtered_names = [
        name for i,name in enumerate(row.names.split(';'))
        if i not in overlap_index
    ]

    # Only keep those with exactly one name match
    if len(filtered_names) != 1:
        continue

    name = unidecode(filtered_names[0]).lower()
    bad_name_codes = [
        "fellowship",
        "trust",
        "grant",
        "author",
        "project",
        "pharmaceutical",
        "institute",
        "university",
        "hospital",
        "global",
        "marie curie",
    ]

    if any(code in name for code in bad_name_codes):
        continue

    # Require at least two names
    if len(name.split()) == 1:
        continue
    
    first_name = name.split()[0]

    if first_name not in known_names:
        continue

    g_score = gender.loc[first_name, 'score']

    data.append({
        "PMCID":pmcid,
        "sentence":row.sentence,
        "gender_score":g_score,
        "name":name,
    })


data = pd.DataFrame(data).set_index("PMCID")
data.to_csv(f_save)
print(f"Found {len(data):,} out of {len(df):,} single named sentences") 
