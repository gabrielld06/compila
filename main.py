from antlr4 import *
from tngLexer import tngLexer
from tngParser import tngParser
from tngVisitor import tngVisitor
from tngSemantical import tngSemantical

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
for tk in token_list:
    print(tk)

parser = tngParser(token_stream)

# Parse the input file and create the syntax tree
tree = parser.inicio()

# Traverse the syntax tree using the custom visitor object
visitor = tngSemantical()
visitor.visit(tree)
print(visitor.symbolTable)
print(visitor.errors)