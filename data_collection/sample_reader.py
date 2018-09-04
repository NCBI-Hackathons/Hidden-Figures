import tarfile
import bs4

f_PMC = 'sources/articles.C-H.xml.tar.gz'

with tarfile.open(f_PMC, 'r:gz') as TAR:
    for f in TAR:

        # Skip item if a directory
        if f.isdir():
            continue

        # Extract the file to IOBuffer and read it
        raw = TAR.extractfile(f).read()

        # Parse the XML
        soup = bs4.BeautifulSoup(raw, 'lxml')

        # Find and print the acknowledgments
        print soup.find('ack')


