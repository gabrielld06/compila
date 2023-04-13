from antlr4 import *
from tngLexer import tngLexer
from tngParser import tngParser
from tngVisitor import tngVisitor
from tngSemantic import tngSemantic
import os, subprocess, sys
import inspect # print(inspect.getmembers(token.getTokenSource(), predicate=inspect.ismethod)) # get class methods

def main():
    if(len(sys.argv) > 1):
        inputFile = sys.argv[1]
        print(f"Compilando o arquivo '{inputFile}'")
    else:
        inputFile = 'tests/test.tng'
        print("Nenhum arquivo foi definido para compilação, compilando '/tests/test.tng'")
        print("Para compilar um arquivo específico: 'python3 tngCompiler.py <nomeDoArquivo>'")

    # Abrir arquivo de input
    with open(inputFile, 'r') as f:
        input_stream = InputStream(f.read())

    # Criar analisador léxico para o input
    lexer = tngLexer(input_stream)
    # Obter a lista de tokens
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()
    token_list = token_stream.tokens

    # ID / START:END POSITION = TOKEN_TXT / TOKEN_TYPE / LINHA:COLUNA
    # for tk in token_list:
    #     print(tk)

    # Analisador sintático
    parser = tngParser(token_stream)
    # Criar a árvore sintática
    tree = parser.inicio()

    if parser.getNumberOfSyntaxErrors() > 0:
        print('Errors were found. Exiting compiler...')
        sys.exit(0)

    # Realizar a análise semântica ao explorar a árvore sintática 
    visitor = tngSemantic()
    visitor.visit(tree)
    # print(visitor.symbolTable)
    # print(visitor.errors)
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

if __name__ == '__main__':
   main()
