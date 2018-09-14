import os, glob
import numpy as np
import spacy as sp
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
import time

'''
For all tags matching, this will replace the contents with this value. Useful
to remove math, inline-links, emails, etc...
'''
__tag_replace_key = "__FILTERED_TAG"

'''
Initialize spaCy. The 'xx' dataset is the biggest multilanguage one.  
It catches the most names. The 'en' dataset does the best job of parsing 
organizations and labels verbs and other parts of speech. Install model 
with `python -m spacy download en`
'''
nlp = sp.load('en')

load_dest = 'extracted/'
save_dest = 'parsed/'
os.system(f'mkdir -p {save_dest}')
cutoff = 50

F_CSV = glob.glob(os.path.join(load_dest,'*.csv'))
print(f"Found {len(F_CSV)} files to parse.")

# These were determined by hand from tag_analysis/TITLE_counts.csv

filtered_tags = '''
Funding
Availability of data and materials
Competing interests
Authors’ contributions
Ethics approval and consent to participate
Consent for publication
Open Access
Conflict of Interests
Conflict of interest
Compliance with ethical guidelines
Disclosures
Ethics approval
Conflicts of interest
Disclosure
Compliance with Ethics Guidelines
Article Information
Author contributions
Authors’ contribution
Authors' contributions
Author’s contributions
Conflict of Interest
Disclosure of Potential Conflicts of Interest
Author Contributions
Authors' Contribution
Competing interest
Disclaimer
Declarations
Consent to publish
Competing Interests
Authors’ Contributions
Availability of supporting data
Ethical approval
Data Availability
Compliance with ethics guidelines
Consent
Funding information
Financial support
Declaration of Interests
Ethical standards
Conflict of interest statement
Declaration of interest
Human and Animal Rights and Informed Consent
Authorship
Informed consent
Supplementary data
Conflict of interest and funding
Availability of Data and Materials
Ethics and consent to participate
Availability of data and supporting materials
Funding sources
Conflict of interests
Declaration
Ethical standard
Contributors
Availability of data
Ethical approval and consent to participate
'''.strip().split('\n')

# These were determined by hand from tag_analysis/total_tag_counts.csv

replace_tags = '''
ext-link
award-id
email
inline-formula
funding-source
uri
'''.strip().split('\n')

# These should not be in any names
bad_count_nouns = [
    'University',
    'Research',
    'Number',
    'Doctoral',
    'Postdoc',
    'Scientist',
    'Data',
    'Surgeon',
    'Centre',
    'Center',
    'Foundation',
    'Universidad',
    'Microscop',
    'Microbio',
    'Agency',
    'Management',
    'ACKNOWLEDGMENT',
    'Acknowledgement',
    'Initiative',
    'Survey',
]


def parse_row(row):
    
    if (row.Acknowledgment_Tag is None or
        type(row.Acknowledgment_Tag) == float):
        
        return []
    
    soup = BeautifulSoup(row.Acknowledgment_Tag,'lxml')

    for tag in replace_tags:
        for match in soup.find_all(tag):
            match.replace_with(__tag_replace_key)

    text = soup.get_text(separator=' ')
    doc = nlp(text)

    data = []
    
    for sent in doc.sents:

        item = {
            "filename":row.filename,
            "sentence":sent,
            "names":list(),
        }
        
        for ele in nlp(sent.text).ents:
            name = ele.text.strip()
            label = ele.label_

            if label != "PERSON":
                continue

            # Remove if any bad matching words
            if any(word.lower() in name.lower()
                   for word in bad_count_nouns):
                continue

            # Remove if a number is found
            if any(c.isdigit() for c in name):
                continue

            # If name is in all caps it is unlikely to be a name, or it is 
            # just initals, we can remove it
            if name == name.upper():
                continue

            # Passed all the checks, add this name
            item['names'].append(name)

        # If no names are found, skip this sentence
        if not item["names"]:
            continue

        item["n_names"] = len(item['names'])
        item['names'] = ';'.join(item['names'])
        
        data.append(item)

    return data


data = []

for f in F_CSV:
    df = pd.read_csv(f, nrows=cutoff)
    ITR = tqdm(df.iterrows(), total=len(df))


    for k, row in ITR:
        data.extend(parse_row(row))

f_save = os.path.join(save_dest, 'sentences_with_at_least_one_name.csv')
data = pd.DataFrame(data)

data.to_csv(f_save,index=False)

        

