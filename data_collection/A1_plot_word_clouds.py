import pandas as pd
import collections
import pylab as plt
from wordcloud import WordCloud

df = pd.read_csv("results/gendered_POS_scores_top_results.csv")


# Remove the baseline values for plotting
df = df[df["word"] != "_baseline"]

df = df.set_index('word')
sizes = df["observations"].to_dict()


df['color'] = df.effect_size - df.effect_size.min()
df.color /= df.color.max()

def gender_color_func(
        word, font_size, position, orientation, random_state=None,
        **kwargs
):
    c = df.loc[word]['color'].mean()
    print(c)

    c = int(255*c)
    return (256-c,c,256-c)


WC = WordCloud(
    background_color='white',
    width=600,
    height=400
).generate_from_frequencies(sizes)

#print (sizes)

WC.recolor(color_func=gender_color_func)
plt.imshow(WC, interpolation='bilinear')
plt.axis('off')
plt.show()
