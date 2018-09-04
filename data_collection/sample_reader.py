import tarfile
from tqdm import tqdm
import bs4

f_PMC = 'sources/articles.C-H.xml.tar.gz'

with tarfile.open(f_PMC, 'r:gz') as TAR:

    # This parses about 20 files per second on a single core
    for f in tqdm(TAR):

        # Skip item if a directory
        if f.isdir():
            continue

        # Extract the file to IOBuffer and read it
        raw = TAR.extractfile(f).read()

        # Parse the XML
        soup = bs4.BeautifulSoup(raw, 'lxml')

        # Find and print the acknowledgments
        # returns None if tag isn't found
        print (soup.find('ack'))


