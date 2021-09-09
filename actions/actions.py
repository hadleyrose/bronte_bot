# This files contains your custom actions which can be used to run
# custom Python code.

import wikiquote
import random
from nltk.corpus import wordnet as wn

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# base data for actions

# store Bronte names
emily = 'Emily Brontë'
charlotte = 'Charlotte Brontë'
anne = 'Anne Brontë'
branwell = 'Branwell Brontë'
brontes = [branwell, charlotte, emily, anne]

# Get all quotes per Bronte
results = {bronte: wikiquote.quotes(bronte, max_quotes=100) for bronte in brontes}


class ActionRandomGreeting(Action):

    def name(self) -> Text:
        return "action_random_greeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get quotes containing lemma
        # get greeting lemma
        tests = [str(i).replace('_', ' ').replace('-', ' ') for syn in wn.synset('greeting.n.01').hyponyms() for i in syn.lemma_names()]
        
        # exact quote matches for greeting lemma
        greetings = [(bronte, test, quote) for bronte, result in results.items() for quote in result for w in quote.split() for test in tests if test == w.lower()]

        # get random quote
        quote = random.choice(greetings)

        dispatcher.utter_message(text=f"{quote[2]} \n {quote[0]}")

        return []
