1) Setup project with .gitignore and .gitattributes
2) Create environment
   1) `conda create --name bronte_bot_env`
   2) `conda activate bronte_bot_env`
   3) `conda install -c conda-forge python=3.8 spacy nltk` -- see note here: https://forum.rasa.com/t/getting-rasa-command-not-found/23405/11
   4) `python -m spacy download en_core_web_lg`
   5) Downloaded nltk wordnet corpus
      ```python
      import nltk
      nltk.download('wordnet')
      ```
   6) `pip install rasa wikiquote`
1) Specified environment package builds and versions in `bronte_bot_env.yml` using `conda env export > bronte_bot_env.yml`
2) Initialize project structure
   1) `rasa init` -- enabled in current directory, trained an initial model based on provided data and setup, tested on CLI
3) Tested and updated default custom action
   1) Uncommented custom action in `actions.py` and formatted utter message as f-string to return date and time
   2) Added custom action to `domain.yml` in new actions section
   3) Added custom action to stories -- happy path
   4) Updated `test_stories.yml` to test custom action
   5) Uncommented `action_endpoint` in `endpoints.yml`
   6) Tested use of action. Action server functioned from outset, but for rasa bot to use custom action, I had to retrain
      1) `rasa train`
      2) In one terminal, run `rasa run actions`. In separate terminal, run `rasa tests` to generate test results on `test_stories.yml` or run `rasa shell` to test ad-hoc user interaction
4) Created `action_random_greeting` in `actions.py`
   1) Modified `actions.py` to utilize wikiquote, random, and wordnet to pull and generate a random "greeting" quote from a Bronte
   2) Incorporated new `action_random_greeting` into `domain.yml` actions, `stories.yml` stories, and `test_stories.yml`
   3) Re-trained rasa model, ran into errors based on environment changes, resolved (below), and re-trained
   4) Ran actions server and bot and confirmed random quote activity
   5) Ran test_stories to confirm expected behavior of `action_random_greeting`