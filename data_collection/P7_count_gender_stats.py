import pandas as pd

cutoff = 10**20

info = pd.read_csv(
    "results/PMC_ack_stats.csv",
    usecols=["n_people"],
    nrows=cutoff)

print(f"Mean/median people on ack",
          info.n_people.mean(), info.n_people.median())

df = pd.read_csv(
    "parsed/single_named_sentences_POS.csv",
    nrows=cutoff,
    usecols=["PMCID","gender_score"],
)
df = df.set_index("PMCID")

idx = pd.isnull(df.gender_score)
print(f"Fraction of PMCID sentences without a gender {idx.mean()}") 
print(
    f"Fraction of women on single sentence gender scores",
    df.gender_score.mean())

