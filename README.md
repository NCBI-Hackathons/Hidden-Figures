# Hidden Figures

### Project Overview
An investigation into the acknowledgments section of research articles within [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/).
Prior literature suggests there is a gender discrepancy between men and women in authorship and acknowledgment. 
Specifically, it has been observed that women were more likely to be acknowledged rather than the author list, in a small sample of  [theoretical population genetics publications](https://www.biorxiv.org/content/early/2018/07/05/360933). We tested this observation  on a large-scale across biomedical research articles and investigated the contributions of acknowledged individuals.

### Background
Few large-scale studies have been conducted on acknowledgments in research articles; our study is novel in size and scope. Notable previous studies: 

![Khabsa et al 2012](https://github.com/NCBI-Hackathons/Hidden-Figures/blob/master/figures/Khabsa%20clip.PNG)
- extracted acknowledgments sections from articles in [CiteSeerX](http://citeseer.ist.psu.edu/index;jsessionid=75C159A83DB7C9F3624F934430F5F3E7)
- identified individuals and organizations
- build network graph of acknowledged entities and authors

![Paul-Hus et al 2017](https://github.com/NCBI-Hackathons/Hidden-Figures/blob/master/figures/Paul-Hus%20clip.PNG)
- extracted acknowledgements sections from articles in [Web of Science](https://clarivate.com/products/web-of-science/)
- identified acknowledged contributions
- analyzed trends in contributions by field of study



### Observations

Call the PubMed Cental subset with acknowledgments PMCA.

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
