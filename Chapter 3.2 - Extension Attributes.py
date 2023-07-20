
# Learning NLP With spaCy Course's Python Library
# Chapter 3: Processing Pipelines


import spacy
nlp = spacy.blank("en")
nlp = spacy.load('C:/Users/DELL/AppData/Local/Programs/Python/Python311/Lib/site-packages/en_core_web_sm/en_core_web_sm-3.5.0')
print()


# C) EXTENSION ATTRIBUTES


# STEP 1: ATTRIBUTE EXTENSIONS
# IMPORT GLOBAL CLASSES
from spacy.tokens import Token
# SET EXTENSION ON THE TOKEN WITH DEFAULT VALUE
Token.set_extension("is_color", default=False)
doc = nlp("The sky is blue.")
# OVERWRITE EXTENSION ATTRIBUTE VALUE
doc[3]._.is_color = True

# STEP 2: PROPERTY EXTENSIONS NO. 1
# DEFINE GETTER FUNCTION
def get_is_color2(token):
    colors = ["red", "yellow", "blue"]
    return token.text in colors
# SET EXTENSION ON THE TOKEN WITH GETTER
Token.set_extension("is_color2", getter=get_is_color2)
doc = nlp("The sky is blue.")
print(doc[3]._.is_color2, "-", doc[3].text)

# STEP 3: PROPERTY EXTENSIONS NO. 2
from spacy.tokens import Span
# DEFINE GETTER FUNCTION
def get_has_color(span):
    colors = ["red", "yellow", "blue"]
    return any(token.text in colors for token in span)
# SET EXTENSION ON THE SPAN WITH GETTER
Span.set_extension("has_color", getter=get_has_color)
doc = nlp("The sky is blue.")
print(doc[1:4]._.has_color, "-", doc[1:4].text)
print(doc[0:2]._.has_color, "-", doc[0:2].text)

# STEP 4: METHOD EXTENSIONS
from spacy.tokens import Doc
# DEFINE METHOD WITH ARGUMENTS
def has_token(doc, token_text):
    in_doc = token_text in [token.text for token in doc]
    return in_doc
# SET EXTENSION ON THE DOC WITH METHOD
Doc.set_extension("has_token", method=has_token)
doc = nlp("The sky is blue.")
print()
print(doc._.has_token("blue"), "- blue")
print(doc._.has_token("cloud"), "- cloud")
print()


# D) SCALING AND PERFORMANCE


# STEP 1: PASSING IN CONTEXT NO. 1
data = [
    ("This is a text", {"id": 1, "page_number": 15}),
    ("And another text", {"id": 2, "page_number": 16}),
]
for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["page_number"])
print()

# STEP 2: PASSING IN CONTEXT NO. 2
from spacy.tokens import Doc
Doc.set_extension("id", default=None)
Doc.set_extension("page_number", default=None)
data = [
    ("This is a text", {"id": 1, "page_number": 15}),
    ("And another text", {"id": 2, "page_number": 16})
]
for doc, context in nlp.pipe(data, as_tuples=True):
    print(doc.text, context["page_number"])
print()

# STEP 3: USING ONLY THE TOKENISER
# BAD:
doc = nlp("Hello world!")
# GOOD:
doc = nlp.make_doc("Hello world!")