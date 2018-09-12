# Hidden Figures

An investigation into the acknowledgments section of research articles within [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/).
Prior literature suggests there is a gender discrepancy between males and females concerning authorship and acknowledgment. 
Specifically, it has been noted that females are more likely to be on an acknowledgement than the author list, though the prior studies involve small samples. 
We seek to test this claim across NIH-funded biomedical research and investigate what roles those listed in the acknowledgments performed.

### Observations

Call the PubMed Cental subset with acknowledgements PMCA.

+ Number of pubs in PMCA with authors with idenifiable genders: 312,237
+ Fraction of females in PMCA in the acks: 0.424 
+ Fraction of females on PMCA in the pubs: 0.233
+ Median number of people on an ack: 5
+ Most acks are uni-gender, 80%
+ Most of these uni-gender acks are all-male 202150 vs 47105

### Hypothesis

1. Women are more likely to be on the acknowledgments than the author list would suggest.
2. The acknowledgment for the types tasks for men and women differ.
3. The type of praise given men and women differ (_fruitful_ discussion, _outstanding_ analysis).
4. These trends change over time, reflecting more equality.

### Timeline / Tasks

+ [x] Download and hash source dataset
+ [x] Literature search
+ [x] [data_collection](data_collection/): Extract acknowledgments text and analyze counts
+ [X] NER names
+ [X] Evaluate hypothesis #1
+ [ ] Extract job titles/tasks
+ [ ] Evaluate hypothesis #2
+ [ ] NER entities
+ [ ] Evaluate hypothesis #3

### Data Sources

[PMC FTP](https://www.ncbi.nlm.nih.gov/pmc/tools/ftp/)

### Data Wrangling

The PMC XML files seem to have a `<ack>` tag as the Acknowledgments.
For example, consider [PMC 4959138](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4959138/):

```
<ack>
    <p>
	We thank Alexia Prskawetz for the fruitful discussions and remarks. 
	Further on, we would like to thank the referees and editors for their 
	valuable comments. This research was partly supported by the Austrian 
	Science Fund (FWF) under Grant No. P25979-N25 and is an extract out of 
	the Ph.D. thesis (Moser <xref ref-type="bibr" rid="CR30">2014</xref>).
    </p>
</ack>
```

### Contributors

+ [Travis Hoppe](https://github.com/thoppe)
+ [Rebecca Meseroll](https://github.com/rmeseroll)
+ [Hao Yu](https://github.com/summer66)
+ [Abbey Zuehlke](https://github.com/zuehlkead)
+ [Grant Jones](https://github.com/grantdjones)
+ [Brad Busse](https://github.com/facepalm)
