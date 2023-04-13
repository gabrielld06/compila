
@echo off
set arg=%1
set arqEntrada=%2

if %arg%==compile (
    java -jar antlr-4.12.0-complete.jar *.g4 -Dlanguage=Python3 -visitor
)
if %arg%==tree (
    java -jar antlr-4.12.0-complete.jar tng.g4 -visitor
    javac *.java -cp antlr-4.12.0-complete.jar
    move /Y *.class javaFiles/
    move /Y *.java javaFiles/
    if "%arqEntrada%"=="" (
        echo Nenhum arquivo foi especificado.
        echo Gerando arvore sintatica de "tests/test.tng".
        java -cp antlr-4.12.0-complete.jar;./javaFiles org.antlr.v4.gui.TestRig tng inicio tests/test.tng -gui
    ) else (
        echo Gerando arvore sintatica de %arqEntrada%.
        java -cp antlr-4.12.0-complete.jar;./javaFiles org.antlr.v4.gui.TestRig tng inicio %arqEntrada% -gui
    )
)
if %arg%==help (
    echo %~nx0 compile - Gera os arquivos de análise lexica e sintatica com a ferramenta
    echo %~nx0 tree <nomeDoArquivo> - Exibe a arvore sintatica do programa do arquivo dado
)