import pandas as pd
import numpy as np
import pylab as plt
import seaborn as sns
from wordcloud import WordCloud

cmap_female  = sns.light_palette("purple", n_colors=256)
cmap_male  = sns.light_palette("green", n_colors=256)

df = pd.read_csv("results/gendered_POS_scores_top_results.csv")

# Remove the baseline values for plotting, and set the index
df = df[df["word"] != "_baseline"].set_index('word')

# Set two different scales for female and males so they scale the same
df['is_female'] = df.effect_size > 0

idx_female = df.is_female>0
df.loc[idx_female, "effect_size"] -= df.loc[idx_female, "effect_size"].min()
df.loc[idx_female, "effect_size"] /= df.loc[idx_female, "effect_size"].max()

df.loc[~idx_female, "effect_size"] *= -1
df.loc[~idx_female, "effect_size"] -= df.loc[~idx_female, "effect_size"].min()
df.loc[~idx_female, "effect_size"] /= df.loc[~idx_female, "effect_size"].max()

# Scale the size to be proportional to the log of the observations times a power of the effect
sizes = (df["observations"]*(df["effect_size"])**3).to_dict()

def gender_color_func(word,  **kwargs):

    is_female = df.loc[word].is_female.mean()>0

    # Choose the correct colormap
    cmap = cmap_female if df.loc[word].is_female.mean() > 0 else cmap_male

    # Pick the color out of the colormap
    c_int = int(df.loc[word]['effect_size'].mean()*255)
    return tuple((cmap[c_int]*255).astype(int))


WC = WordCloud(
    background_color='white',
    width=600,
    height=400
).generate_from_frequencies(sizes)

WC.recolor(color_func=gender_color_func)
plt.imshow(WC, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.show()
