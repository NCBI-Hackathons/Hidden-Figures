Access dates:

```
-rw-rw-r-- 1 hoppeta hoppeta  5817271380 Sep  6 11:39 articles.A-B.xml.tar.gz
-rw-rw-r-- 1 hoppeta hoppeta  6843338714 Sep  6 11:27 articles.C-H.xml.tar.gz
-rw-rw-r-- 1 hoppeta hoppeta  8789517680 Sep  6 11:33 articles.I-N.xml.tar.gz
-rw-rw-r-- 1 hoppeta hoppeta 11068643003 Sep  6 11:36 articles.O-Z.xml.tar.gz
```

File Hashes:

```
md5sum *.gz
333b8d420a924dbce6f8f47db408fc3b  articles.A-B.xml.tar.gz
b30f87a8b28246f05678a1d0d5324a8c  articles.C-H.xml.tar.gz
c8c421d596bbd2685ccece074f76ba9a  articles.I-N.xml.tar.gz
0fc411c9f4789dff3fb31b8ec4c61f2f  articles.O-Z.xml.tar.gz
```

Extracted reference sizes:

```
Saved to extracted/articles.A-B.xml.tar.gz.csv
Found 209856 out of 378845 acknowledgments

Saved to extracted/articles.C-H.xml.tar.gz.csv
Found 235079 out of 464167 acknowledgments

Saved to extracted/articles.I-N.xml.tar.gz.csv
Found 325844 out of 653444 acknowledgments

Saved to extracted/articles.O-Z.xml.tar.gz.csv
Found 402376 out of 610080 acknowledgments
```

Simple parsing results

Total PMC articles: 2,106,536
Has Acknowledgements: 1,174,911    
Percent True    55.77%

# Parsed results, per publication

```
         n_sentences       n_people
count  747525.000000  747525.000000
mean        1.742841       4.285726
std         2.014077       9.891483
min         1.000000       1.000000
25%         1.000000       1.000000
50%         1.000000       3.000000
75%         2.000000       5.000000
max       375.000000    2424.000000
```

# Examples of very high people counts

```
PLoS_Med/PMC4380415.nxml	228	2424
PLoS_One/PMC4411156.nxml	50	2197
Surg_Endosc/PMC6061087.nxml	139	1435
PLoS_One/PMC4605674.nxml	51	1111
Crit_Care/PMC6097245.nxml	319	1009
Crit_Care/PMC5998562.nxml	275	996
```
