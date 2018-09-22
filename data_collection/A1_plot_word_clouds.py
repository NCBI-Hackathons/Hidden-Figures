import pandas as pd
import collections
import pylab as plt
from wordcloud import WordCloud

df = pd.read_csv("results/gendered_POS_scores_top_results.csv")


# Remove the baseline values for plotting
df = df[df["word"] != "_baseline"]

sizes = df.set_index("word")["observations"].to_dict()


def gender_color_func(
        word, font_size, position, orientation, random_state=None,
        **kwargs
):
    gender = word_gender(word)
    gender = int(255*gender)
    #print (word,gender)
    return (256-gender,gender,256-gender)#"hsl(0, 0%%, %d%%)" % random.randint(60, 100)


WC = WordCloud(
    background_color='white',
    width=600,
    height=400
).generate_from_frequencies(sizes)

#print (sizes)
#wordcloud.recolor(color_func=gender_color_func)
plt.imshow(WC, interpolation='bilinear')
plt.axis('off')
plt.show()
