import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("GitHub Codespaces makes development easy.")
for token in doc:
    print(token.text, token.pos_, token.dep_)
