# Compiladores - TNG

## Compiladores - CC UEM 2023

Implementação de um compilador para a linguagem TNG, criada para este trabalho.
Dividida nas etapas de:

-   Análise Léxica
-   Análise Sintática
-   Análise Semântica
-   Geração de Código

A geração de código será feita para a linguagem C++.

### Execução

- Instalar todas as dependências com o comando "pip install -r requirements.txt"
  - Requer g++ para compilar o código gerado em C++
  - Foi utilizado Python na versão 3.10 para o desenvolvimento do trabalho
- Para gerar os arquivos de análise léxica e sintática, use o comando "antlr.bat compile"
- Para gerar a árvore sintática de um programa, use o comando "antlr.bat tree \<nomeDoArquivo\>"
  - Caso não seja fornecido um arquivo de entrada, "tests/test.tng" é utilizado por padrão
- Para executar o compilador com um arquivo de entrada, use "python3 tngCompiler.py \<nomeDoArquivo\>"
  - Caso não seja fornecido um arquivo de entrada, "tests/test.tng" é compilado por padrão
  - O arquivo C++ resultante é nomeado "output.cpp"
  - O arquivo executável resultante é nomeado "output.exe"
- Finalmente, executar o programa compilado com "./output"
