
# Learning NLP With spaCy Course's Python Library
# Chapter 1: Finding Words, Phrases, Names and Concepts


# IMPORT LIBRARIES
import spacy
print()


# A) INTRODUCTION TO SPACY


# 1: THE NLP OBJECT
# CREATE A BLANK ENGLISH NLP PROJECT
nlp = spacy.blank("en")

# 2: THE DOC OBJECT
# CREATED BY SPACY BY PROCESSING A STRING OF TEXT WITH THE NLP PROJECT
doc = nlp("Hello world!")
# ITERATE OVER TOKENS IN A DOC
for token in doc:
    print(token.text)
    print()

# 3: THE TOKEN OBJECT
# INDEX INTO THE DOC TO GET A SINGLE TOKEN
token = doc[1]
# GET A TOKEN TEXT VIA THE .TEXT ATTRIBUTE
print(token.text)
print()

# 4: THE SPAN OBJECT
# A SLICE FROM THE DOC IS A SPAN OBJECT
span = doc[1:3]
# GET THE SPAN TEXT VIA THE .TEXT ATTRIBUTE
print(span.text)
print()

# 5: LEXICAL ATTRIBUTES
# ITERATE OVER THE TOKENS IN THE DOC
doc = nlp("It costs $5.")
print("It costs $5.")
print("Index:   ", [token.i for token in doc])
print("Text:    ", [token.text for token in doc])
print()
print("Is a word:", [token.is_alpha for token in doc])
print("Is a punctuation:", [token.is_punct for token in doc])
print("Is a number:", [token.like_num for token in doc])
print()


# B) TRAINED PIPELINES


# 1: PIPELINE PACKAGES
# LOAD THE SMALL ENGLISH PIPELINE
nlp = spacy.load('C:/Users/DELL/AppData/Local/Programs/Python/Python311/Lib/site-packages/en_core_web_sm/en_core_web_sm-3.5.0')

# 2: PREDICTING PART-OF-SPEECH TAGS
# PROCESS A TEXT
doc = nlp("She ate a pizza")
# ITERATE OVER THE TOKENS
for token in doc:
    # PRINT THE TEXT AND THE PREDICTED PART-OF-SPEECH TAG
    print(token.text, token.pos_)
print()

# 3: PREDICTING SYNTACTIC DEPENDENCIES
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
print()

# 4: PREDICTING NAMED ENTITIES
# PROCESS A TEXT
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
print("Text: \nApple is looking at buying U.K. startup for $1 billion. \n")
# ITERATE OVER THE PREDICTED ENTITIES
for ent in doc.ents:
    # PRINT THE ENTITY TEXT AND ITS LABEL
    print(ent.text, ent.label_)
print()

# TIP: THE SPACY.EXPLAIN METHOD
# GET QUICK DEFINITIONS OF THE MOST COMMON TAGS AND LABELS
print("Explain \"GPE\": ")
print(spacy.explain("GPE"))
print()
print("Explain \"NNP\": ")
print(spacy.explain("NNP"))
print()
print("Explain \"dobj\": ")
print(spacy.explain("dobj"))
print()


# C) RULE-BASED MATCHING


# STEP 1: USING THE MATCHER
# IMPORTING THE MATCHER
from spacy.matcher import Matcher
# LOAD A PIPELINE AND CREATE THE NLP PROJECT
nlp = spacy.load('C:/Users/DELL/AppData/Local/Programs/Python/Python311/Lib/site-packages/en_core_web_sm/en_core_web_sm-3.5.0')
# INITIALISE THE MATCHER WITH THE SHARED VOCAB
matcher = Matcher(nlp.vocab)
# ADD THE PATTERN TO THE MATCHER
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", [pattern])
# PROCESS SOME TEXT
doc = nlp("Upcoming iPhone X release date leaked")
# CALL THE MATCHER ON THE DOC
matches = matcher(doc)
# ITERATE OVER THE MATCHES
for match_id, start, end in matches:
    # GET THE MATCHED SPAN
    matched_span = doc[start:end]
    print(matched_span.text)
print()

# STEP 2: MATCHING LEXICAL ATTRIBUTES
pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]
matcher.add("FIFA_World_Cup", [pattern])
doc = nlp("2018 FIFA World Cup: France won!")
matches = matcher(doc)
for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)
print()

# STEP 3: MATCHING OTHER TOKEN ATTRIBUTES
pattern = [
    {"LEMMA": "love", "POS": "VERB"},
    {"POS": "NOUN"}
]
matcher.add("DOGS_AND_CATS", [pattern])
doc = nlp("I loved dogs but now I love cats more.")
matches = matcher(doc)
for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)
print()

# STEP 4: USING OPERATORS AND QUANTIFIERS
pattern = [
    {"LEMMA": "buy"},
    {"POS": "DET", "OP": "?"},  # optional: match 0 or 1 times
    {"POS": "NOUN"}
]
matcher.add("BUYING_STUFF", [pattern])
doc = nlp("I bought a smartphone. Now I'm buying apps.")
matches = matcher(doc)
for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)
print()