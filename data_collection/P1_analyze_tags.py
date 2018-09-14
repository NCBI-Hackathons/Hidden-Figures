import os, glob
import numpy as np
import pandas as pd
from tqdm import tqdm
import collections
from bs4 import BeautifulSoup
import joblib


load_dest = 'extracted/'
save_dest = 'tag_analysis/'
os.system(f'mkdir -p {save_dest}')

cutoff = 10**20



F_CSV = glob.glob(os.path.join(load_dest,'*.csv'))
print(f"Found {len(F_CSV)} files to parse.")

decompose_tags = set([
    "ext-link", "email",
    "tex-math", "inline-formula", "term", 
])

ignored_tags = set([
    "p", "italic", "bold", "underline", "list",
    "list-item", "xref", "sup", "sec", "sub",
    "array", "sc", "def", "def-item", "td", "tr", "term-head", "def-head",
    "tbody", "def-list", "award-id", "uri", "col", "th",
    "inline-graphic", "col-group",  "thead", "table-wrap", "pub-id",
    "named-content",
])

count_tags = set([
    "title", "funding-source", "grant-sponsor",
])

def parse_row(row):
    
    simple_counts = collections.Counter()
    structured_counts = collections.defaultdict(collections.Counter)
    
    if row.Acknowledgment_Tag is None or type(row.Acknowledgment_Tag) == float:
        return simple_counts, structured_counts
    
    soup = BeautifulSoup(row.Acknowledgment_Tag, 'lxml').ack

    # Count all documents
    simple_counts['__total_documents'] += 1
    
    for item in soup.find_all():
        name = item.name
        simple_counts[name] += 1

        if name in count_tags:
            text = item.get_text().strip()
            structured_counts[name][text] += 1

    return simple_counts, structured_counts

simple_counts = collections.Counter()
structured_counts = collections.defaultdict(collections.Counter)

for f in F_CSV:
    df = pd.read_csv(f, nrows=cutoff)

    for k,row in tqdm(df.iterrows(), total=len(df)):

        s0, s1 = parse_row(row)
        simple_counts.update(s0)

        for key in s1:
            structured_counts[key].update(s1[key])



f_simple = os.path.join(save_dest, 'total_tag_counts.csv')
df = pd.Series(simple_counts, name="observations")
df = df.sort_values(ascending=False)
df.to_csv(f_simple, header=True, index_label="tag")

            
for key,val in structured_counts.items():
    df = pd.Series(val, name="observations")
    df = df.sort_values(ascending=False)

    name_key = key.upper()
    f_csv = os.path.join(save_dest, f'{name_key}_counts.csv')
    df.to_csv(f_csv, header=True, index_label="tag")                  
