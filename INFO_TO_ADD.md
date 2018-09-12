# Quality control

| Acknowledgment Name Parsing Error | Occurrence |PMCID | Example
|--|--|--|--
| Author's Name Listed  | 4.5% | [PMC3339585](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3339585/) | **Smriti Shrivastava** is thankful to CSIR for Senior Research Fellowship
| Fellowship Name|2.0%|[PMC5864053](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5864053/)|J.S. was funded by a Biotechnology and Biological Sciences Research Council (BBSRC) **David Phillips Fellowship** (BB/L024551/1)
|Organization Name |2.0%|[PMC4160263](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4160263/)|National Institute of Biomedical Imaging and Bioengineering Grant R01 EB006745 **Stanford Bio-X**, the American Heart Association (Western States Affiliates)
| Award Name | 1.5% |[PMC4189622](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4189622/)|**Seed Grant** provided by Michigan Technological University (MTU)
| Disclosure | 1.5% |[PMC4147052](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4147052/)|In addition, **Jin Jin** also holds stock in Eli Lilly
| Dedication | 0.5% |[PMC4831668](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4831668/)|This paper is dedicated to **José Luis García Ruano** on occasion of his retirement

# Figures

![](figures/ack_counts.png | width=300)
Counts of PMC articles with/without acknowledgments.

![](figures/Ack_absent_wordcloud.png |width=300)
MeSH terms in abstracts more prevalent in PMC articles _without_ an acknowledgment.

![](figures/Ack_present_wordcloud.png |width=300)
MeSH terms in abstracts more prevalent in PMC articles _with_ an acknowledgment.


Gender specific word clouds used in the acknowledgment section. Colored by gender, purple are dominantly male, green predominately female, grey is used equally by both genders. Sized by word frequency -- gender specific words were preferentially selected.

![](figures/cloud_gendered_nouns.png|width=300)

![](figures/cloud_gendered_verbs.png|width=300)

We manually developed a list of keywords that grouped the types of acknowledgement into four categories: Materials, Analysis, Procedure, Advice. For each category, we calculated the representation of female names:

| Category | Fraction of female names|
|--|--|
|material| 0.378|
|analysis| 0.414|
|procedure| 0.447|
|advice| 0.326|

Both the word cloud and keyword summaries show that men are more likely to be thanked for their discussion and advice, while women are more likely to be thanked for the work performed in both the laboratory and the manuscript.