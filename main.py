from antlr4 import *
from tngLexer import tngLexer
from tngParser import tngParser
from tngVisitor import tngVisitor
from tngSemantic import tngSemantic
import os, subprocess, sys
import inspect # print(inspect.getmembers(token.getTokenSource(), predicate=inspect.ismethod)) # get class methods

# Open the input file
with open('tests/test.tng', 'r') as f:
    input_stream = InputStream(f.read())

# Create a lexer for the input
lexer = tngLexer(input_stream)

# Get the list of tokens
token_stream = CommonTokenStream(lexer)
token_stream.fill()
token_list = token_stream.tokens

# ID / START:END POSITION = TOKEN_TXT / TOKEN_TYPE / LINHA:COLUNA
# for tk in token_list:
#     print(tk)

parser = tngParser(token_stream)

# Parse the input file and create the syntax tree
tree = parser.inicio()

if parser.getNumberOfSyntaxErrors() > 0:
    print('Errors were found. Exiting compiler...')
    sys.exit(0)

# Traverse the syntax tree using the custom visitor object
visitor = tngSemantic()
visitor.visit(tree)
print(visitor.symbolTable)
print(visitor.errors)
# print(visitor.code)

if visitor.compile():
    with open("output.cpp", "w") as out:
        out.write(visitor.code)
        myEnv = os.environ.copy()
        myEnv["PATH"] = myEnv["PATH"]+";"+os.path.abspath("external/mingw64")
        command = ["g++.exe", "output.cpp", "-std=c++17", "-Os", "-o", "output"]
        process = subprocess.Popen(command, shell=True, env=myEnv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out.close()
        print('Output compiled successfully')
else:
    print('Errors were found. Exiting compiler...')