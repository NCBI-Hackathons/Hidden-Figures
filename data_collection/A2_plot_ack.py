import pandas as pd

cutoff = 10**20
df = pd.read_csv("parsed/PMID_PMCID_pubYear.csv", nrows=cutoff)
df = df[df["Pub Year"] <= 2017]
df = df[df["Pub Year"] >= 1980]

g0 = df[df.has_ack==True].groupby("Pub Year").size()
g1 = df.groupby("Pub Year").size()

dx = pd.DataFrame()
dx['Total_PMCID_counts'] = g1
dx['Pubs_with_Proper_Acknowledgements'] = g0
dx.to_csv("results/Number_of_Ack_per_Year.csv")

import pylab as plt
import seaborn as sns

plt.plot(g0,marker='o',label=f'Proper Acknowledgments ({g0.sum():,})')
plt.plot(g1,marker='o',label=f'PMC publications ({g1.sum():,})')
plt.legend()
plt.ylabel("Publication Count")
plt.xlabel("Publication Year")
plt.title("Acknowledgment counts on PMC publications (1980-2017)")

sns.despine()
plt.tight_layout()

plt.savefig("results/Number_of_Ack_per_Year.png")

plt.show()


