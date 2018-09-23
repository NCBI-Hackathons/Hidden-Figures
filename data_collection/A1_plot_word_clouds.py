import pandas as pd
import numpy as np
import os
import pylab as plt
import seaborn as sns
from wordcloud import WordCloud

n_colors = 256
cmap_female  = sns.light_palette("green", n_colors=n_colors+1)
cmap_male  = sns.light_palette("purple", n_colors=n_colors+1)

save_dest = 'results/'


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

def gender_color_func(word,  **kwargs):

    is_female = POS.loc[word].is_female.mean()>0

    # Choose the correct colormap
    cmap = cmap_female if POS.loc[word].is_female.mean() > 0 else cmap_male

    # Pick the color out of the colormap
    c = POS.loc[word]['effect_size'].mean()
    c = np.clip(1.4*c, 0, 1) # exemplify differences
    c_int = int(c*n_colors)
    return tuple((cmap[c_int]*n_colors).astype(int))


for part_of_speech, POS in df.groupby("part_of_speech"):

    # Scale the size to be proportional to the log of the observations
    # times a power of the effect

    scale_power = {
        "ADJ"  : 0.5,
        "NOUN" : 1.0,
        "VERB" : 1.0,
    }
    
    sizes = (POS["observations"]*
             POS["effect_size"]**scale_power[part_of_speech]).to_dict()
    
    WC = WordCloud(
        background_color='white',
        width=600,
        height=400
    ).generate_from_frequencies(sizes)

    WC.recolor(color_func=gender_color_func)

    plt.figure()
    plt.imshow(WC, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()

    f_png = os.path.join(save_dest, f"wordcloud_{part_of_speech}.jpg")
    plt.savefig(f_png, bbox_inches='tight', pad_inches=0, dpi=200)
    plt.title(part_of_speech)

#plt.show()
