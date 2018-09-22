import pandas as pd
import collections
import pylab as plt
from wordcloud import WordCloud

df = pd.read_csv("results/gendered_POS_scores_top_results.csv")


# Remove the baseline values for plotting
df = df[df["word"] != "_baseline"]

sizes = df["observations"].to_dict()


WC = WordCloud(
    background_color='white',
    width=600,
    height=400
).generate_from_frequencies(sizes)

print (sizes)
