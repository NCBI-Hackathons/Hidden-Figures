"""Extract acknowledgment data from a PMC tar file, files can be found at
ftp://ftp.ncbi.nlm.nih.gov/pub/pmc

Usage:
  P0_parse_XML.py <f_PMC>

Options:
  -h --help     Show this screen.
  <f_PMC>       input .xml.tar.gz file
"""

import tarfile
from tqdm import tqdm
import bs4
import os
import pandas as pd
import joblib
from docopt import docopt


def iterate_GZ_file(f_GZ):
    
    with tarfile.open(f_GZ, 'r:gz') as TAR:

        # This parses about 20 files per second on a single core
        for k, f in enumerate(tqdm(TAR)):
            
            # Skip item if a directory
            if f.isdir():
                continue

            # Extract the file to IOBuffer and read it
            raw = TAR.extractfile(f).read()

            yield f.path, raw

            # Cutoff to help debuging
            # if k>100:break

def extract_information(f, raw):

    # Parse the XML
    soup = bs4.BeautifulSoup(raw, 'lxml')

    # Find and print the acknowledgments
    # returns None if tag isn't found
    ack = soup.find('ack')

    if ack is None:
        ack = ""

    return f, str(ack)


def process_PMC_file(f_PMC):
    # In parallel we become IO/bound, but process speed is ~300 records/s

    save_dest = "extracted"
    os.makedirs(save_dest, exist_ok=True)
    f_save = os.path.join(save_dest, os.path.basename(f_PMC) + '.csv')
    
    ITR = iterate_GZ_file(f_PMC)
    with joblib.Parallel(-1) as MP:
    
        func = joblib.delayed(extract_information)

        data = []
        for f, ack in MP(func(f, raw) for f, raw in ITR):
            data.append({"filename":f, "Acknowledgment_Tag":ack})

    df = pd.DataFrame(data).set_index('filename')
    df.to_csv(f_save)

    print(f"Saved to {f_save}")

    is_valid = ~(df.Acknowledgment_Tag == "")
    print(f"Found {is_valid.sum()} out of {len(df)} acknowledgments")



if __name__ == "__main__":
    args = docopt(__doc__)
    process_PMC_file(args['<f_PMC>'])


