
# Learning NLP With spaCy Course's Python Library
# Chapter 3.1: Processing Pipelines


import spacy
nlp = spacy.blank("en")
nlp = spacy.load('C:/Users/DELL/AppData/Local/Programs/Python/Python311/Lib/site-packages/en_core_web_sm/en_core_web_sm-3.5.0')
print()


# A) PROCESSING PIPELINES


# STEP 1: PIPELINE ATTRIBUTES
print(nlp.pipe_names)
print()
print(nlp.pipeline)
print()


# B) CUSTOM PIPELINE COMPONENTS


# STEP 1: ANATOMY OF A COMPONENT
from spacy.language import Language
@Language.component("custom_component")
def custom_component_function(doc):
    # DO SOMETHING TO THE DOC HERE
    return doc
nlp.add_pipe("custom_component")

# STEP 2: EXAMPLE | A SIMPLE COMPONENT
# CREATE THE NLP OBJECT
nlp = spacy.load('C:/Users/DELL/AppData/Local/Programs/Python/Python311/Lib/site-packages/en_core_web_sm/en_core_web_sm-3.5.0')
# DEFINE A CUSTOM COMPONENT
@Language.component("custom_component")
def custom_component_function(doc):
    # PRINT THE DOC'S LENGTH
    print("Doc length:", len(doc))
    # RETURN THE DOC OBJECT
    return doc
# ADD THE COMPONENT FIRST IN THE PIPELINE
nlp.add_pipe("custom_component", first=True)
# PRINT THE PIPELINE COMPONENT NAMES
print("Pipeline:", nlp.pipe_names)
print()

# STEP 3: EXAMPLE 2 | A SIMPLE COMPONENT
# CREATE THE NLP OBJECT
nlp = spacy.load('C:/Users/DELL/AppData/Local/Programs/Python/Python311/Lib/site-packages/en_core_web_sm/en_core_web_sm-3.5.0')
# DEFINE A CUSTOM COMPONENT
@Language.component("custom_component")
def custom_component_function(doc):
    # PRINT THE DOC'S LENGTH
    print("Doc length:", len(doc))
    # RETURN THE DOC OBJECT
    return doc
# ADD THE COMPONENT FIRST IN THE PIPELINE
nlp.add_pipe("custom_component", first=True)
# PROCESS A TEXT
doc = nlp("Hello world!")