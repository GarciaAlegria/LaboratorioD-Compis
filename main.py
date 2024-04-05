from readyalex import *
from arbol import *
from dfa_directly import *


# Se toma el filename
print("=======================================================")
filename = "./tests/slr-3.yal"
# Se obtiene el filereader
file_reader = File(filename)
# Se obtiene la regex
regex = file_reader.regex
tokens = file_reader.tokens_list
print(regex)
print(tokens)
