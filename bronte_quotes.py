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
