
# Learning NLP With spaCy Course's Python Library
# Chapter 2: Large-scale Data Analysis With spaCy


import spacy
nlp = spacy.blank("en")
print()


# A) DATA STRUCTURES NO. 1: VOCAB, LEXEMES AND STRINGSTORE


# STEP 1: HASH VALUES
nlp.vocab.strings.add("coffee")
coffee_hash = nlp.vocab.strings["coffee"]
coffee_string = nlp.vocab.strings[coffee_hash]
# RAISES AN ERROR IF WE HAVEN'T SEEN THE STRING BEFORE
string = nlp.vocab.strings[3197928453018144401]

# STEP 2: LOOK UP THE STRING AND HASH IN NLP.VOCAB.SETTINGS
doc = nlp("I love coffee")
print("hash value:", nlp.vocab.strings["coffee"])
print("string value:", nlp.vocab.strings[3197928453018144401])
print()
# THE DOC ALSO EXPOSES VOCAB AND STRINGS
print("hash value:", doc.vocab.strings["coffee"])
print("string value:", doc.vocab.strings[3197928453018144401])
print()

# STEP 3: LEXEMES: ENTRIES IN THE VOCABULARY
doc = nlp("I love coffee")
lexeme = nlp.vocab["coffee"]
# PRINT THE LEXICAL ATTRIBUTES
print(lexeme.text, lexeme.orth, lexeme.is_alpha)
print()


# B) DATA STRUCTURES NO. 2: DOC, SPAN AND TOKEN


# STEP 1: THE DOC OBJECT
# IMPORT THE DOC CLASS
from spacy.tokens import Doc
# THE WORDS AND SPACES TO CREATE THE DOC FROM
words = ["Hello", "world", "!"]
spaces = [True, False, False]
# CREATE A DOC MANUALLY
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
print()

# STEP 2: THE SPAN OBJECT
# IMPORT THE DOC AND SPAN CLASSES
from spacy.tokens import Doc, Span
# THE WORDS AND SPACES TO CREATE THE DOC FROM
words = ["Hello", "world", "!"]
spaces = [True, False, False]
# CREATE A DOC MANUALLY
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)
print()
# CREATE A SPAN MANUALLY
span = Span(doc, 0, 2)
# CREATE A SPAN WITH A LABEL
span_with_label = Span(doc, 0, 2, label="GREETING")
print(span.text, span.label_)
print()
# ADD SPAN TO DOC.ENTS
doc.ents = [span_with_label]
print([(ent.text, ent.label_) for ent in doc.ents])
print()


# C) WORD VECTORS AND SEMANTIC SIMILARITY


# STEP 1: SIMILARITY EXAMPLES NO. 1
# LOAD A LARGER PIPELINE WITH VECTORS
nlp = spacy.load('C:/Users/DELL/AppData/Local/Programs/Python/Python311/Lib/site-packages/en_core_web_md/en_core_web_md-3.5.0')
# COMPARE TWO DOCUMENTS
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")
print(doc1.similarity(doc2))
print()
# COMPARE TWO TOKENS
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2))
print()

# STEP 2: SIMILARITY EXAMPLES NO. 2
# COMPARE A DOCUMENT WITH A TOKEN
doc = nlp("I like pizza")
token = nlp("soap")[0]
print(doc.similarity(token))
print()
# COMPARE A SPAN WITH A TOKEN
span = nlp("I like pizza and pasta")[2:5]
doc = nlp("McDonalds sells burgers")
print(span.similarity(doc))
print()

# STEP 3: WORD VECTORS IN SPACY
doc = nlp("I have a banana")
# ACCESS THE VECTOR VIA THE TOKEN.VECTOR ATTRIBUTE
print(doc[3].vector)
print()


# D) COMBINING PREDICTIONS AND RULES


# STEP 1: RECAP | RULE-BASED MATCHING
# INITIALISE WITH THE SHARED VOCAB
from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)
# PATTERNS ARE LISTS OF DICTIONARIES DESCRIBING THE TOKENS
pattern = [{"LEMMA": "love", "POS": "VERB"}, {"LOWER": "cats"}]
matcher.add("LOVE_CATS", [pattern])
# OPERATORS CAN SPECIFY HOW OFTEN A TOKEN SHOULD BE MATCHED
pattern = [{"TEXT": "very", "OP": "+"}, {"TEXT": "happy"}]
matcher.add("VERY_HAPPY", [pattern])
# CALLING MATCHER ON DOC RETURNS LIST OF (MATCH_ID, START, END) TUPLES
doc = nlp("I love cats and I'm very very happy")
matches = matcher(doc)

# STEP 2: ADDING STATISTICAL PREDICTIONS
matcher = Matcher(nlp.vocab)
matcher.add("DOG", [[{"LOWER": "golden"}, {"LOWER": "retriever"}]])
doc = nlp("I have a Golden Retriever")
for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print("Matched span:", span.text)
    # GET THE SPAN'S ROOT TOKEN AND ROOT HEAD TOKEN
    print("Root token:", span.root.text)
    print("Root head token:", span.root.head.text)
    # GET THE PREVIOUS TOKEN AND ITS POS TAG
    print("Previous token:", doc[start - 1].text, doc[start - 1].pos_)

# STEP 3: EFFICIENT PHRASE MATCHING
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
pattern = nlp("Golden Retriever")
matcher.add("DOG", [pattern])
doc = nlp("I have a Golden Retriever")
# ITERATE OVER THE MATCHES
for match_id, start, end in matcher(doc):
    # GET THE MATCHED SPAN
    span = doc[start:end]
    print("Matched span:", span.text)