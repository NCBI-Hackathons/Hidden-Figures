import spacy as sp
import pandas as pd
from tqdm import tqdm

cutoff = 10**20
f_csv = "parsed/single_named_sentences.csv"
f_save = "parsed/single_named_sentences_POS.csv"

df = pd.read_csv(f_csv, nrows=cutoff)

nlp = sp.load('en')
keep_POS = set(["NOUN", "VERB", "ADJ"])


def parse_row(k, row):
    doc = nlp(row.sentence)
    item = {"k":k}

    for pos in keep_POS:
        item[pos] = []
    
    for word in doc:
        pos = word.pos_
        
        if pos not in keep_POS:
            continue

        if word.lemma_ == "-PRON-":
            continue

        # Lemmitize the word
        word = str(word.lemma_).lower()

        if not word or not word.isalpha():
            continue
        
        item[pos].append(word)
    
    for pos in keep_POS:
        item[pos] = ';'.join(item[pos])

    return item


data = []

for k, row in tqdm(df.iterrows(), total=len(df)):
    item = parse_row(k, row)
    data.append(item)

data = pd.DataFrame(data).set_index('k')

for col in keep_POS:
    df[col] = data[col]
    
df.to_csv(f_save,index=False)

    
    
