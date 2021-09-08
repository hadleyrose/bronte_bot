# https://pypi.org/project/wikiquote/
import wikiquote
import random

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
