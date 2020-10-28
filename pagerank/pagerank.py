import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    for y in range(3):
        if len(sys.argv) != 2:
            sys.exit("Usage: python pagerank.py corpus")
        for x in range(3):
            corpus = crawl(sys.argv[1] + str(x))
            ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
            print(f"PageRank Results from Sampling (n = {SAMPLES})")
            for page in sorted(ranks):
                print(f"  {page}: {ranks[page]:.4f}")
            ranks = iterate_pagerank(corpus, DAMPING)
            print(f"PageRank Results from Iteration")
            for page in sorted(ranks):
                print(f"  {page}: {ranks[page]:.4f}")
        print('=============== ' + str(y) + '================')


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    rv = {}
    links = corpus.keys()
    pageLinks = [x for x in corpus[page]]
    help = 0
    for link in links:
        if len(pageLinks) == 0:
            rv[link] = 1 / len(links)
            continue
        if link not in pageLinks:
            rv[link] = (1 - damping_factor) / len(links)
        else:
            rv[link] = (damping_factor / (len(pageLinks))) + ((1 - damping_factor) / len(links))
        help += rv[link]
    #print(help, page)
    return rv

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    initial = {}
    theKeys = corpus.keys()
    thePage = randomItem(corpus)
    theLinks = transition_model(corpus, thePage, damping_factor)

    for x in theKeys:
        initial[x] = [(1 / len(corpus))]
    for i in range(n):
        for x in theLinks.keys():
            if x in initial:
                #print(initial[x][0], theLinks[x])
                #initial[x] = (initial[x] + theLinks[x]) / abs(n - i)
                #initial[x][len(initial[x]) - 1])
                #theVal =  initial[x][len(initial[x]) - 1] + (theLinks[x] + ((1 - damping_factor) / len(theLinks))) / initial[x][len(initial[x]) - 1]
                theVal = theLinks[x] #+ ((1 - damping_factor) / len(theLinks))
                initial[x].append(theVal)
        #thePage = randomItem(theLinks)
        thePage = random.choices(list(theLinks.keys()), weights = list(theLinks.values()), k = 1)[0]
        theLinks = transition_model(corpus, thePage, damping_factor)
    help = 0
    for x in theKeys:
        create = initial[x]
        initial[x] = (sum(create) / n)  #+ ((1 - damping_factor) / len(initial[x]))
        #initial[x] = (create * damping_factor) +  ((1 - damping_factor) / n)
        #initial[x] *= damping_factor
        help += initial[x]
    '''print(help)
    print('++++ help ++++')'''
    return initial

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    rv = {}
    for x in corpus.keys():
        rv[x] = ([1 / len(corpus)], False)
    #thePage = random.choices(list(theLinks.keys()), weights = list(theLinks.values()), k = 1)[0]
    thePage = randomItem(corpus)
    theLinks = transition_model(corpus, thePage, damping_factor)
    counter = 1
    while True:
        stopper = True
        for x in theLinks:
            rvList = rv[x][0]
            avr = (sum(rvList) / len(rvList))
            rvList.append(theLinks[x])
            if (abs(sum(rvList) / len(rvList) - avr) < .001):
                rv[x] = (rv[x][0], True)
        for x in corpus.keys():
            if not rv[x][1]:
                stopper = False
                break
        if stopper:
            help = 0
            for x in corpus.keys():
                rv[x] = sum(rv[x][0]) / len(rv[x][0])
                help += rv[x]
            #print(help)
            #print(counter)
            return rv
        else:
            for x in corpus.keys():
                rv[x] = (rv[x][0], False)
            thePage = random.choices(list(theLinks.keys()), weights = list(theLinks.values()), k = 1)[0]
            theLinks = transition_model(corpus, thePage, damping_factor)
        counter += 1
    #raise NotImplementedError

def randomItem(crawl):
    theKeys = crawl.keys()
    key = random.randrange(len(crawl))
    for x in theKeys:
        if key == 0:
            return x
        else:
            key -= 1

if __name__ == "__main__":
    main()
