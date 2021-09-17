# https://pypi.org/project/wikiquote/
import wikiquote
import random
from nltk.corpus import wordnet as wn

# store Bronte names
emily = 'Emily Brontë'
charlotte = 'Charlotte Brontë'
anne = 'Anne Brontë'
branwell = 'Branwell Brontë'
brontes = [branwell, charlotte, emily, anne]

# Get first quote from Emily
wikiquote.quotes(emily, max_quotes=1)

# Get random Branwell quote
random.choice(wikiquote.quotes(branwell))

# Get all quotes per Bronte
results = {bronte: wikiquote.quotes(bronte, max_quotes=100) for bronte in brontes}

# Find a quote containing a word across all Brontes
[quote for result in results.values() for quote in result if 'morning' in quote.lower()]

# Find a quote (and its author) containing a word across all Brontes
print(*[f'{bronte}: {quote}' for bronte, result in results.items() for quote in result if 'doom' in quote.lower()], sep='\n')

# Get source of quote found in results
print(*[bronte for bronte, result in results.items() for quote in result if 'and he said he could not breathe in mine' in quote.lower()])

# Lemma of the word greeting
wn.synset('greeting.n.01').lemma_names()
# Lemma of the hyponyms of the word greeting
print(*[str(i).replace('_', ' ').replace('-', ' ') for syn in wn.synset('greeting.n.01').hyponyms() for i in syn.lemma_names()])

# Get quotes containing lemma
tests = [str(i).replace('_', ' ').replace('-', ' ') for syn in wn.synset('greeting.n.01').hyponyms() for i in syn.lemma_names()]
# fuzzy match -- returns 200 results
print(*[f'{bronte, test}: {quote}' for bronte, result in results.items() for quote in result for test in tests if test in quote.lower()], sep='\n')
# exact word match -- returns 25 results
print(*[f'{bronte, test}: {quote}' for bronte, result in results.items() for quote in result for w in quote.split() for test in tests if test == w.lower()], sep='\n')

# Useful hypernyms
terms = [
    'communication.n.02',
    'message.n.02',
    'acknowledgment.n.03',
    'farewell.n.01'
]

# Lemma of the word greeting
wn.synset('farewell.n.01').lemma_names()
# Lemma of the hyponyms of the word greeting
print(*[str(i).replace('_', ' ').replace('-', ' ') for syn in wn.synset('farewell.n.01').hyponyms() for i in syn.lemma_names()])

# Get quotes containing lemma
tests = [str(i).replace('_', ' ').replace('-', ' ') for syn in wn.synset('farewell.n.01').hyponyms() for i in syn.lemma_names()]
# fuzzy match -- returns 200 results
print(*[f'{bronte, test}: {quote}' for bronte, result in results.items() for quote in result for test in tests if test in quote.lower()], sep='\n')
# exact word match -- returns 25 results
print(*[f'{bronte, test}: {quote}' for bronte, result in results.items() for quote in result for w in quote.split() for test in tests if test == w.lower()], sep='\n')

def hyponym_quote_finder(
    token_wordnet_tag: str,
    source: str or list = None,
    fuzzy: bool = False,
    fuzzy_if: bool = True,
    threshold = 10
) -> list:
    # full result set
    quotes = results

    # narrow result set if specified
    if source:
        if isinstance(source, str):
            quotes = {bronte: quote for bronte, quote in quotes.items() if source == bronte}
        
        if isinstance(source, list):
            quotes = {bronte: quote for bronte, quote in quotes.items() if bronte in source}

    # get token_wordnet_tag lemma
    tests = [str(i).replace('_', ' ').replace('-', ' ') for syn in wn.synset(token_wordnet_tag).hyponyms() for i in syn.lemma_names()]

    # Get quotes containing lemma

    # exact word match
    matches = [(bronte, test, quote) for bronte, result in quotes.items() for quote in result for w in quote.split() for test in tests if test == w.lower()]

    if fuzzy or (fuzzy_if and len(matches) < threshold):
        # fuzzy match
        matches = [(bronte, test, quote) for bronte, result in quotes.items() for quote in result for test in tests if test in quote.lower()]

    return matches
