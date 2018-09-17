import pandas as pd
import numpy as np
import pylab as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

cutoff = 10**20

f_csv = "parsed/sentences_with_at_least_one_name.csv"
cols = ['filename', 'n_names']
df = pd.read_csv(f_csv, usecols=cols, nrows=cutoff)


g = df.groupby("filename")

n_pubs = len(g.size())
print (f"Total number of pubs with ack {n_pubs}")

info = pd.DataFrame()
info["n_sentences"] = g.size()
info["n_people"] = g["n_names"].sum()

print(info.describe())
info.to_csv("results/PMC_ack_stats.csv")

for key in info.columns:
    val = info[key].quantile(q=0.95)
    idx = info[key] > val
    info.ix[idx, key] = val+1


ax = plt.figure(figsize=(16/2., 9/2.)).gca()
hist_kws={"rwidth":0.75, 'alpha':0.75, 'align':'left'}

bins = np.arange(1, len(info.n_sentences.unique()) + 2)


sns.distplot(info.n_sentences, kde=False, bins=bins, hist_kws=hist_kws)
#plt.xlim(xmin=1)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.tight_layout()
plt.xlabel("Number of acknowledgment sentences with people per article")
plt.ylabel("Number of PMC articles")
sns.despine()
plt.tight_layout()

plt.savefig("results/Number_of_Sentences_on_Ack.png")


ax = plt.figure(figsize=(16/2., 9/2.)).gca()
bins = np.arange(1, len(info.n_people.unique()) + 2)

sns.distplot(info.n_people, kde=False, bins=bins, hist_kws=hist_kws)
#plt.xlim(xmin=1)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.xlabel("Number of people per publication in acknowledgments")
plt.ylabel("Number of PMC articles")
sns.despine()
plt.tight_layout()

plt.savefig("results/Number_of_People_on_Ack.png")
plt.show()
