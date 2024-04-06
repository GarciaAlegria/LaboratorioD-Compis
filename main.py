from readyalex import *
from arbol import *
from dfa_directly import *
from scanner_producer import *

# Se toma el filename
print("=======================================================")
filename = "slr-3.yal"
# Se obtiene el filereader
file_reader = File(filename)
# reguex y tokens
regex = file_reader.regex
tokens = file_reader.tokens_list
print("=======================================================")
print("=======================================================")
print("Reguex")
print(regex)
print("=======================================================")
print("=======================================================")
print("Tokens")
print(tokens)
# Se crea el AFD
afd = afdConstruction(regex, "Yalex 3")
afd.simulation("token_test.txt")
ScannerProducer(afd, "Yalex_3", tokens)