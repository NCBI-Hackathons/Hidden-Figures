import pandas as pd
import collections
from scipy.stats import binom_test
from tqdm import tqdm

_min_obervations = 10
POS = ["NOUN", "VERB", "ADJ"]

df = pd.read_csv(
    "parsed/single_named_sentences_POS.csv",
    usecols=POS + ["gender_score"],
    nrows=10**20,
)

counts = collections.defaultdict(collections.Counter)
gender = collections.defaultdict(collections.Counter)

for pos in POS:

    counts[pos]["_baseline"] = len(df)
    gender[pos]["_baseline"] = df.gender_score.sum()

    words = df[~pd.isnull(df[pos])]

    ITR = zip(words.gender_score, words[pos])
    for g, word_list in tqdm(ITR, total=len(words)):
        
        for word in word_list.split(';'):
            counts[pos][word] += 1
            gender[pos][word] += g


info = {}

for pos in POS:

    dx = pd.DataFrame(index=counts[pos].keys())
    dx.index.name = "word"
    dx["observations"] = pd.Series(counts[pos])
    dx["net_gender_score"] = pd.Series(gender[pos])
    dx["part_of_speech"] = pos
    dx = dx.reset_index().set_index(["word", "part_of_speech"])
    info[pos] = dx

df = pd.concat(info.values())

df["avg_gender_score"] = df.net_gender_score / df.observations
del df["net_gender_score"]

df = df.sort_values('observations', ascending=False)

# Require a minimum number of observations
df = df[df.observations >= _min_obervations]

expected = df.loc[["_baseline","NOUN"], "avg_gender_score"].mean()
p_value = [binom_test(x*n,n,p=expected) for x,n in
           tqdm(zip(df.avg_gender_score, df.observations))]
df["p_value"] = p_value


print(df)
df.to_csv("results/gendered_POS_scores.csv")
