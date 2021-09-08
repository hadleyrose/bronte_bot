1) Setup project with .gitignore and .gitattributes
2) Create environment
   1) `conda create --name bronte_bot_env`
   2) `conda activate bronte_bot_env`
   3) `conda install -c conda-forge python=3.8 spacy` -- see note here: https://forum.rasa.com/t/getting-rasa-command-not-found/23405/11
   4) `python -m spacy download en_core_web_lg`
   5) `pip install rasa`
   6) `pip install wikiquote`
3) Initialize project structure
   1) `rasa init` -- enabled in current directory, trained an initial model based on provided data and setup, tested on CLI