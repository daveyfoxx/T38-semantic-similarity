# The cat, monkey and banana example was interesting 
# as it showed a much closer similarity between cats and monkeys
# than cats and bananas. 

# This is conceivable as cats and monkeys are both animals and mammals
# and cats and bananas have no close logical connection. 

# MY EXAMPLE: 

# Importing spaCy for nlp
import spacy

# Storing our language model in a variable
nlp = spacy.load('en_core_web_sm')

# running our words through the language model and storing it
tokens = nlp("cannon horse gun grass water oxygen")

# Nested for loop for accessing and comparing our words similarity
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# COMPARING LANGUAGE MODELS FROM EXAMPLE FILE:

# I found it interesting that the 'en_core_web_sm' model
# has no word vectors included, and only uses context-sensitive tensors.

# This means it may not always provide us with useful similarity judgements.
# Whereas, the 'en_core_web_md' model does include these. 